"""
模块导入
内置模块：python内部已经写好的模块
自己写的模块
别人写的模块

requests 仓库，安装
pip
"""

# 导入requests
import requests
# 访问url接口地址,发送一个get请求
# url = "http://api.github.com"
# res = requests.get(url)
# print(res)
# # 获取返回信息
# print(res.text)
# 如何传递参数，如何修改请求头，token
headers = {"token":"123","username":"yuze"}
url = "http://api.github.com"
# res = requests.get(url,headers=headers)

# 如何传递参数，位置参数，或者关键字参数params
data = {"username":"xianren","pwd":"123456"}
res = requests.get(url,params=data,headers=headers)

print(res)