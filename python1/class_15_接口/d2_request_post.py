import requests
url = "http://localhost:5000/login"
headers = {"dalao":"y","sing_dog":"yuz"}
# 如何传递参数，params,query_string的形式传递的
data = {"username":"flybird","admin":"bawa"}
# res = requests.post(url,headers=headers,params=data)

# 传递参数2：表单形式传递
form_data = {"form_admin":"benben"}
# res = requests.post(url,headers=headers,data=form_data)
# 传递参数3：json
json_data = {"json_data":"jay"}
# res = requests.post(url,headers=headers,json=json_data)

"""
1.response对象
响应报文，需要什么从这里取
断点调试，有哪些信息

2.结果获取
1>.text
2>.content
3>.json{}
4>cookie,获取cookie
如果不是json呢？报错
如果不想让他报错？重新封装
"""
res = requests.post(url,headers=headers,params=data)
# 获取相应文本，得到的数据类型：string
# print(res.text)

# 获取二进制形式的(图片)
# print(res.content)

# 获取json,响应数据不是json，响应就会报错，加try: except
# json得到的是字典数据类型
print(type(res.json()))