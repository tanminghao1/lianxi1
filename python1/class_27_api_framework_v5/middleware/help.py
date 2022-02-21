import re

import ddt
from jsonpath import jsonpath

from common.db_handler import DBHandler
from common.request_handler import RequestHandler
from config.setting import config
from middleware.yaml_handler import yaml_data

# 封装一个登录操作

def login():
    """登录返回的是token和member_id
    1.从登录的excel当中读取接口数据
    2.从配置文件中读取
    """
    req = RequestHandler()
    res = req.visit(config.host + '/member/login',
                    'post',
                    json=yaml_data["user"],
                    headers={"X-Lemonban-Media-Type":"lemonban.v2"})
    return res

# def admin_login():
#     pass

# 临时数据类，将项目当中要使用的所有的临时变量存储到Context当中
class Context:
    # token = ''
    member_id = None
    username = ''
    # 动态获取load_id，如果写成方法，getattr就获取不了，只能是属性
    @property  # 加property 将load_id方法设置为一个属性
    def loan_id(self):
        """查询数据库，得到loan_id,
        临时变量保存到Context中
        return 返回load表当中的id值
        """
        db = DBHandler(host=yaml_data['database']['host'],
                  port=yaml_data['database']['port'],
                  user=yaml_data['database']['user'],
                  password=yaml_data['database']['password'],
                  database=yaml_data['database']['database'],
                  charset=yaml_data['database']['charset'])
        loan = db.query("select * from loan where status = 2 limit 10")
        # 关闭游标
        db.close()
        return loan['id']
    @property
    def token(self):
        """
        token属性，而且属性会动态变化
        Context().token 获取token,自动调用这个方法得到token
        :return:
        """
        data = login()
        t = jsonpath(data, '$..token')[0]
        token_type = jsonpath(data, '$..token_type')[0]
        # 拼接token
        t = " ".join([token_type, t])
        return t
    @property
    # 要动态获取不同用户的话写成方法，property不能传参数
    def member_id(self):
        data = login()
        m_id = jsonpath(data,'$..id')[0]
        return m_id
# 通过将token获取写到Context中作为动态属性，不需要再为函数调用获取
def save_token():
    """保存token信息"""
    data = login()
    token = jsonpath(data,'$..token')[0]
    token_type = jsonpath(data,'$..token_type')[0]
    member_id = jsonpath(data,'$..id')[0]

    # 拼接token
    token = " ".join([token_type,token])
    # 将token设置到context属性中
    Context.token = token
    Context.member_id = member_id
    return [token,member_id]

# 正则表达式匹配并替换
def replace_label(target):
    """用data替换target里的标签
    {"mobile_phone":"*phone*"} ==> {"mobile_phone":"137"}
    """
    """while循环"""
    re_pattern = r'#(.*?)#'
    while re.findall(re_pattern,target):
        # 如果能够匹配,再通过search匹配一次得到要替换的key，进行动态替换
        key = re.search(re_pattern,target).group(1)
        # 使用getattr动态设置并获取属性值，转换为字符串类型替换
        target = re.sub(re_pattern,str(getattr(Context(),key)),target,1)
    return target

if __name__ == '__main__':
    # data = login()
    # token = data['data']['token_info']['token']
    # token_type = data['data']['token_info']['token_type']
    # # jsonpath, ==>专门用来解析json的路径工具
    # # 1.安装jsonpath库  pip install
    # # 2.引入
    # # 3.返回的是列表，通过索引获取
    # token1 = jsonpath(data,'$..token')[0]
    # token_type1 = jsonpath(data,'$..token_type')[0]
    # id = jsonpath(data,'$..id')[0]
    """
    $   表示根节点
    .   表示子节点,查询子节点字段
    ..  表示子孙节点,查询所有层级字段
    """

    # data = save_token()
    print(Context().token)