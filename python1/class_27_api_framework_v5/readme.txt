readme 文件。
对项目进行说明。

1.环境安装
-安装python
-pip install
-添加 excel
-python ......py运行程序

2.对项目的版本进行更新说明


# 发邮件
# 记录log
# 动态数据的处理
# 测试用例的关联
# 正则表达式
# 数据库状态

# logger
# yaml

配置文件：
1. py文件  非常灵活，只有python能用
2. yaml   通用，读取解析简洁智能
3. ini 读取比较复杂，以前用的多，很多历史遗留项目主要使用这种方式

框架的分层：
1.runtest.py : 作用：代码入口，收集测试用例，生成测试报告
2.测试逻辑test_cases包： 各个模块便于管理和维护
3.数据管理层data:excel数据 yaml
4.业务逻辑层（request_handler,excel_handler）通用的logger,访问数据库
5.配置文件（和项目是相关联的，项目地址，数据库地址，logger级别）
6.测试报告（输出）

动态数据：
注册功能中正确的手机号码不能提前知道，需要通过程序去动态生成

充值接口：
-，前置条件登录的实现方式：
1.setup， self.req.visit()访问登录接口，res得到token
2.

接口base_url: http://120,78.128.25:8766/futuureloan
mysql数据库连接信息：
主机：120.78.128.25
port:3306
用户:future
密码：123456
库名：futureloan

master