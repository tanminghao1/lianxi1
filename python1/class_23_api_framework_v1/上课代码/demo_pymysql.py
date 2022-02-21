"""
python 操作数据库：
mysql,oracle,sqlsever,mongodb,access,

操作MySQL数据库，db-api,pymysql驱动

1.建立连接  conn = pymysql.connect()
2.建立游标 cursor = conn.cursor()
3.执行sql，cursor.excute()
4.获取结果 cursor.fechone()  cursor.fechall()
5.关闭游标和连接 cursor.close() conn.close()
"""

import pymysql

# 建立连接
# TODO:utf-8 要写成utf8
from pymysql.cursors import DictCursor

host='120.78.128.25'
port=3306
user='future'
password='123456'
charset='utf8'
database='futureloan'

conn = pymysql.connect(host='120.78.128.25',port=3306,
                       user='future',password='123456',
                       charset='utf8',database='futureloan',
                       cursorclass=DictCursor
                       )
print(conn)

# 游标，数据库操作当中一个重要的概念,采取行动
cursor = conn.cursor()

# 执行sql语句
cursor.execute('select * from member limit 2;')

# 获取游标结果,共用一个游标进行多次查询时游标会移动，第二个查询结果会不一样
one = cursor.fetchone()   # 拿到第一行数据
all = cursor.fetchall()  # 拿到除第一行外的所有数据
print(one)
print(all)
# 游标cursor默认拿到的数据为元组类型，可以在建立连接初始化时设置为字典类型，cursorclass=DictCursor

# 创建一个新的游标
cursor_other = conn.cursor()
cursor_other.execute('select * from member limit 2;')
all2 = cursor_other.fetchall()
print(all2)

# 使用后关闭游标和连接
cursor.close()
cursor_other.close()
conn.close()


conn2 = pymysql.connect(host=host,port=port,
                        user=user,password=password,
                        database=database,
                        charset='utf8',
                        cursorclass=DictCursor
                        )
cursor = conn2.cursor()
cursor.execute("select * from member limit2 ")
cursor.fetchone()
cursor.close()
conn2.close()

















# 1.建立连接
conn3 = pymysql.connect(host=host,port=port,
                        user=user,password=password,
                        charset='utf8',
                        database=database,
                        cursorclass=DictCursor)
# 2.初始化游标
cursor3 = conn3.cursor()
# 3.执行查询语句
cursor3.execute("select * from member limit2;")
# 4.获取查询数据
cursor3.fetchall()
# 5.关闭游标和连接
cursor3.close()
cursor3.close()


conn4 = pymysql.connect(host=host,port=port,
                        user=user,password=password,
                        database=database,
                        cursorclass=DictCursor,
                        charset="utf8")
cursor4 = conn4.cursor()
cursor4.execute("select * from member limit2;")
cursor4.fetchall()
cursor4.close()
conn4.close()


