import requests

# 注册接口
# url = 'http://120.78.128.25:8766/futureloan/member/register'
# headers = {"X-Lemonban-Media-Type":"lemonban.v1"}
# data = {"mobile_phone":"18111111111","pwd":"12345678"}
# # 一定要添加headers关键字参数，不可作为位置参数传递
# # content-type不需要添加，json关键字参数就是表示：content-type:json
# # data关键字参数就是表示 表单格式
# # params关键字参数表示query string格式
# res = requests.post(url,headers=headers,json=data)
# print(res.json())

# 登录接口
# token放在什么地方
# token可以放到请求体
url = 'http://test.lemonban.com/futureloan/mvc/api/member/login'
headers = {"X-Lemonban-Media-Type":"lemonban.v2"}
data = {"mobile_phone":"18111111111","pwd":"12345678"}
res = requests.post(url,headers=headers,json=data)
print(res.json())

# 充值接口，需要传递token
token = res.json()['data']['token_info']['token']
id = res.json()['data']['id']
headers ={"X-Lemonban-Media-Type":"lemonban.v2","Authorzation":"Bearer {}".format(token)}
data = {
    "member_id":id,
    "amount":100
}
res = requests.post(url,headers=headers,json=data)

