# 如何传递cookie，sessionid作为cookie发送到服务端进行session校验
# 一个session,一次会话对象
# 1.每开一次浏览器（关闭浏览器默认session过期，浏览器可以设置）
# session(jsession='ggiugiugiu')

# 如何操作cookie
import requests
# 登录
login_url = 'http://test.lemonban.com/futureloan/mvc/api/member/login'
data = {"mobilephone":"18111111111","pwd":"123456"}
res = requests.get(login_url,data)
print(res.json())

# 获取cookie,如果通过浏览器会自动带上cookie
# cookies =res.cookies
# 充值
# recharge_url = 'http://test.lemonban.com/futureloan/mvc/api/member/recharge'
# recharge_data = {"mobilephone":"18111111111","amount":"1000"}
# res = requests.post(recharge_url,data=recharge_data,cookies=cookies)
# print(res.text)

# session,直接使用session，会自动带上cookie
# 1.登录
# se = requests.Session()
session = requests.sessions.session()
login_url = 'http://test.lemonban.com/futureloan/mvc/api/member/login'
data = {"mobilephone":"18111111111","pwd":"123456"}
res = session.post(login_url,data)
print(res.json())

# 2.充值
recharge_url = 'http://test.lemonban.com/futureloan/mvc/api/member/recharge'
recharge_data = {"mobilephone":"18111111111","amount":"1000"}
res = session.post(recharge_url,data=recharge_data)
print(res.text)

# 再次充值，初始化了另外的session(重新打开会话，需要重新登录)
# another_session = requests.sessions.session()
# res = another_session.post(recharge_url,data=recharge_data)
# print(res.text)