from jsonpath import jsonpath

from common.request_handler import RequestHandler
from config.setting import config
from middleware.yaml_handler import yaml_data


def login():
    """登录返回的是token和member_id
    1.从登录的excel当中读取接口数据
    2.从配置文件中读取
    """
    req = RequestHandler()
    res = req.visit(config.host + '/member/login',
                    'post',
                    json=yaml_data['user'],
                    headers={"X-Lemonban-Media-Type":"lemonban.v2"})
    return res

# 临时数据类，将项目当中要使用的所有的临时变量存储到Context当中
class Context:
    token = ''
    member_id = None



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

    data = save_token()
    print(data)