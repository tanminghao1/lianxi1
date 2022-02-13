import json
import unittest
import yaml

from common.db_handler import DBHandler
from common.helper import generate_mobile
from common.logger_handler import LoggerHandler
from libs import ddt
from common.excel_handler import ExcelHandler
from common.request_handler import RequestHandler
from config.setting import config

# yaml读取
f = open(config.yaml_config_path,encoding='utf-8')
yaml_data = yaml.load(f,Loader=yaml.FullLoader)

"""注册相关用例"""
@ddt.ddt
class TestRegister(unittest.TestCase):
    # 读取数据
    excel_handler = ExcelHandler(config.data_path)
    data = excel_handler.read('register')
    logger = LoggerHandler(name=yaml_data['logger']['name'],
                           level=yaml_data['logger']['level'],
                           file=yaml_data['logger']['file']
                           )

    def setUp(self) -> None:
        self.req = RequestHandler()
        # self.db =DBHandler(host=yaml_data['database']['host'],
        #           port=yaml_data['database']['port'],
        #           user=yaml_data['database']['user'],
        #           password=yaml_data['database']['password'],
        #           database=yaml_data['database']['database'],
        #           charset=yaml_data['database']['charset']
        #           )
    def tearDown(self) -> None:
        self.req.close_session()
        # self.db.close()
    @ddt.data(*data)
    def test_register(self,test_data):
        # print(test_data)

        # # 判断test_data['json']如果出现#exist_phone#，使用generate_mobile生成手机号码
        # # 随机生成一个手机号码，替换#exist_phone#
        # if '#exist_phone#' in test_data['json']:
        #     # mobile = generate_mobile()
        #     # 查询数据库，如果数据库当中存在该手机号，那我们直接使用这个手机号？
        #     # 直接查询数据库，随机找一个，直接使用该号码替换
        #     mobile = self.db.query("select * from member limit 1;")
        #     if mobile:
        #         # 替换
        #         test_data['json'] = test_data['json'].replace("#exist_phone#",mobile['mobile_phone'])
        #     else:
        #         # 随机生成一个，但数据库中还是不存在
        #         # 可以在helper写个注册的方法，直接调用注册过的手机号
        #         pass
        # # 生成新的手机号码
        # if '#new_phone#' in test_data['json']:
        #     while True:
        #         gen_mobile = generate_mobile()
        #         # 查询数据库，如果数据库中存在该手机号码，那么我们再生成一次，直到不存在为止
        #         mobile = self.db.query("select * from member where mobile_phone=%s;",args=[gen_mobile])
        #         if not mobile:
        #             break
        #     test_data['json'] = test_data['json'].replace('#new_phone#',gen_mobile)

        # 访问接口，得到实际结果
        res = self.req.visit(config.host + test_data['url'],
                             test_data['method'],
                             headers = json.loads(test_data['headers']),
                             json = json.loads(test_data['json'])
                             )
        # 获取预期结果
        # 断言
        try:
            self.assertEqual(json.loads(test_data['excepted'])['code'],res['status'])
            # 测试用例通过时，写入excel数据
            self.excel_handler.write(config.data_path,
                                     'register',
                                     test_data['case_id']+1,
                                     9,
                                     '测试通过')
        except AssertionError as e :
            # 记录logger
            self.logger.error(f"测试用例失败：{e}")
            # 测试用例失败时写入excel结果
            self.excel_handler.write(config.data_path,
                                     'register',
                                     test_data['case_id']+1,
                                     9,
                                     '测试失败')
            # 手动抛出异常，否则测试用例会自动通过
            raise e
        # 如果出现断言失败，要将失败的用例记录到logger中
        # AssertionError

