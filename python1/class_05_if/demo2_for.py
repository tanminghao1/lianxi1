# 每次判断一个条件 if

# for 循环执行某一段程序
# 循环播放、遍历

songs = ['龙拳','月亮之上','上海滩','葫芦娃','当']
# songs[0]
# songs[1]
# 列表循环
for song in songs:
    # song = songs[0]
    print("正在播放：{}".format(song))
    # index + 1
# 字符串循环
# name = "yuz wang"
# for i in name:
#     print(i,end='/')   #end以什么结束
# 字段循环遍历
# 字典默认是获取keys

name = {"name":"yuz","age":18}
for i in name.keys():
    print(i)
# 如果想获取values，加values
for m in name.values():
    print(m)
# 如果想获取key和values
for n in name.items():
    print(n)    #输出(key,value)元组
# 获取key，value每个，通过元组解包方式 a,b = ("1","2")
for k,j in name.items():
    print(k)
    print(j)
