"""
1.单元测试框架，unitest
2.什么是单元测试：函数，类
3.单元测试是谁去测试，开发测试
4.单元测试框架和我们的接口测试有什么区别

如何判断结果：断言，判断预期结果和实际结果是否相等
"""
# 访问接口
import requests
url = "http://localhost:5000/login"
headers = {"dalao":"y","sing_dog":"yuz"}
data = {"username":"flybird","admin":"bawa"}

def visitor(url,headers,data):
    res = requests.post(url,headers=headers,params=data)
    return res.text


# 断言 1+1==2
# 断言
# assert 1 + 2 ==5
# print("assert finished")

# assert本质上是一种异常机制，会抛出异常