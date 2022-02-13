# 封装requests
import requests
class HttpHandler:
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
