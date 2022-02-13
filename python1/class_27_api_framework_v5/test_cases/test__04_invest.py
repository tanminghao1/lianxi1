import json
import unittest
import yaml
from mock import Mock

from common.db_handler import DBHandler
from common.helper import generate_mobile
from common.logger_handler import LoggerHandler
from libs import ddt
from common.excel_handler import ExcelHandler
from common.request_handler import RequestHandler
from config.setting import config
from middleware.help import Context
from middleware.yaml_handler import yaml_data
# yaml读取,直接调用yaml封装后初始化的对象,不需要去初始化
# f = open(config.yaml_config_path,encoding='utf-8')
# yaml_data = yaml.load(f,Loader=yaml.FullLoader)


"""投资相关用例"""
@ddt.ddt
class TestInvest(unittest.TestCase):
    # 读取数据
    excel_handler = ExcelHandler(config.data_path)
    data = excel_handler.read('invest')
    logger = LoggerHandler(name=yaml_data['logger']['name'],
                           level=yaml_data['logger']['level'],
                           file=yaml_data['logger']['file']
                           )

    def setUp(self) -> None:
        self.req = RequestHandler()
        self.db =DBHandler(host=yaml_data['database']['host'],
                  port=yaml_data['database']['port'],
                  user=yaml_data['database']['user'],
                  password=yaml_data['database']['password'],
                  database=yaml_data['database']['database'],
                  charset=yaml_data['database']['charset']
                  )

        # 用例关联，充值接口依赖于登录成功
        # 需要先登录，获取token和用户id
        # 结果:
        # 1.直接通过方法调用获取拿到的是字典['token','member_id']
        # save_token()   # 访问登录接口，得到token值和member_id,通过动态属性获取，不再需要调用函数
        # save_loanid() 再封装个获取loanid保存到Context中


        # 通过类属性获取，可以直接拿到值使用，不需要接收函数返回值
        # # 供其他函数调用加self
        # self.token = Context.token
        # self.member_id = Context.member_id
        # print(self.token)
        # print(self.member_id)
    def tearDown(self) -> None:
        self.req.close_session()
        self.db.close()
    @ddt.data(*data)
    def test_invest(self,test_data):
        """投资接口"""
        # 1.替换json数据当中的member_id，  "#member_id#" 替换成Context.member_id
        # 2.访问接口，得到实际结果
        # 3.断言实际结果 == 预期结果

        # 可以直接在测试方法中直接调用存储在context中的参数
        token = Context.token
        member_id = Context.member_id

        # 查询数据库，查询member_id = member_id的用户充值之前的余额
        sql = 'select * from member where id = %s;'
        user = self.db.query(sql,args=[member_id])
        beformoney = user['leave_amount']

        # member_id替换
        if "#member_id#" in test_data['json']:
            # 根据excel中数据是否有引号判断是str还是int
            test_data['json'] = test_data['json'].replace("#member_id#",str(member_id))
        # # 错误的用户名，给正确的member_id+1得到一个错误的id
        # if "#wrong_member_id#" in test_data['json']:
        #     test_data['json'] = test_data['json'].replace('#wrong_member_id',str(member_id+1))
        # 需要多个条件语句进行替换时，可以使用正则表达式,一次性完成替换

        # 读取excel当中的headers，得到字典
        headers = json.loads(test_data['headers'])
        # 添加Authorization头信息
        headers['Authorization'] = token


        # # mock,在接口未开发完成时，模拟测试数据{"code":1,"msg":"success"}  res = {"code":1,"msg":"success"}
        # # mock只是为了让整个流程跑通,前期在接口未开发完成时，测试代码编写时使用
        # self.req.visit = Mock(return_value=eval(test_data['expected']))  # 客户端mock,未进行接口请求

        # 得到实际结果
        res = self.req.visit(config.host + test_data['url'],
                         test_data['method'],
                         headers = headers,
                         json = json.loads(test_data['json'])
                             )

        # 断言1：
        self.assertEqual(res['code'],test_data['expected'])
        # 第二次断言：成功用例需要进行数据库校验，金额
        # 判断是否为成功用例，如果是成功用例，校验数据库
        # if test_data['tage'] == "succeess":  1.通过用例标签判断是否为成功用例  2.通过返回码判断是否为成功用例
        if res['code'] == 0:
            # 查看数据库结果，充值金额+充值前余额 == 充值之后的金额
            money = json.loads(test_data['json']['amount'])
            # 获取充值之前的余额，1.写在Context中，获取使用  2.查询数据库，写在visit请求之前
            # 获取充值之后的余额,这里用的游标与上面同一个，会导致查询的beformoney=after_money,需要重新实例化一个游标,
            # 如果在封装db模块中查询后进行commit，则拿到的是最新的数据，不需要再实例化一个新游标
            # self.new_db = DBHandler(host=yaml_data['database']['host'],
            #                     port=yaml_data['database']['port'],
            #                     user=yaml_data['database']['user'],
            #                     password=yaml_data['database']['password'],
            #                     database=yaml_data['database']['database'],
            #                     charset=yaml_data['database']['charset']
            #                     )
            sql = 'select * from member where id = %s;'
            after_user = self.new_db.query(sql, args=[member_id])
            after_money = after_user['leave_amount']
            # self.new_db.close()
            self.assertEqual(beformoney - money,after_money)


# 测试git