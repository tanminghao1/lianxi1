import pymysql
from pymysql.cursors import DictCursor

conn = pymysql.connect(host='120.78.128.25',port=3306,
                       user='future',password='123456',
                       charset='utf8',database='futureloan',
                       cursorclass=DictCursor
                       )

cursor = conn.cursor()

# 执行sql语句
mobile = '13788775654'
# 传递参数的第一种方式:format， 数据发生变动不要用format，防止sql注入
# cursor.execute('select * from member where mobile_phone = {}'.format(mobile))
# 2:args 参数 %s 占坑符,args= 列表或者元组
cursor.execute('select * from member where mobile_phone =%s and id=s%',args=[mobile,33])
user = cursor.fetchone()
print(user)