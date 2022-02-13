# 封装requests
import requests
class RequestHandler:
    def __init__(self):
        self.session = requests.session()

    def visit(self,url,method,params=None,data=None,json=None,**kwargs):
        """访问一个接口，你可以使用get请求，post,put,delete
        请求方法：method
        请求地址：url
        请求参数：params,data,json
        """
        # if method.lower() == 'get':
        #     self.session.get(url,params=params,data=data,**kwargs)
        # elif method.lower() == 'post':
        #     res = self.session.post(url=url,params=params,data=data,json=json,**kwargs)
        # else:
        # request方法可以处理请求方式，只要传method就可以
        res = self.session.request(method,url,params=params,data=data,json=json,**kwargs)
        try:
            return res.json()
        except ValueError:
            print("not json")
    def close_session(self):
        self.session.close()

# test_data =[ {"url":"http://test.lemonban.com/futureloan/mvc/api/member/login",
#               "method":"post",
#               "headers":{"name":"yuz"},
#               "data":{"mobilephone":"18111111111","pwd":"123456"},
#               "expected":"hello word"},
#
#              {"url":"http://test.lemonban.com/futureloan/mvc/api/member/login",
#               "method":"post",
#               "headers":{"name":"yuz"},
#               "data":{"mobilephone":"181111","pwd":"123"},
#               "expected":"hello word"
#              }
#              ]
# data = test_data[0]
# res = RequestHandler().visit(url=data['url'],
#                            method=data['method'],
#                            json=data['data'],
#                            headers=data['headers'])
# print("打印实际返回结果：",res)