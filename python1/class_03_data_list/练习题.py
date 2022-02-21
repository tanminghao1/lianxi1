# 1、统计在一个队列中，有多少个整数和负数
a = [1,-1,3,4,5,6,-9,-2,-5]
b = [i for i in a if i<0]
c = [i for i in a if i>0]
print(len(b))
print(len(c))

n=0
m=0
for i in a:
    if i>0:
        n+=1
    elif i<0:
        m+=1
    else:
        pass
print(n,m)

# 有字符串 "axbyczdj"，如何得到结果“abcd”
a = "axbyczdj"
b = a[::2]
print(b)
c=[]
for i in range(len(a)):
    if i % 2 ==0:
        c.append(a[i])
# 字典转换成字符串
print("".join(c))

# 已知一个字符串为“hello_world_yoyo”, 如何得到一个队列
# ["hello","world","yoyo"]
a = "hello_world_yoyo"
c=a.split("_")
print(c)

# 已知一个队列,如： [1, 3, 5, 7], 如何把第一个数字，放到第三个位置，得到：
# [3, 5, 1, 7]
a = [1,3,5,7]
a.insert(2,a[0])
print(a[1:])

# 已知 a = 9, b = 8,如何交换 a 和 b 的值，得到 a 的值为 8,b 的值为 9
a,b=b,a
c =a
a=b
b=c

# 打印出 100-999 所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数
# 字立方和等于该数本身。例如：153 是一个"水仙花数"，因为 153=1 的三次方＋
# 5 的三次方＋3 的三次方
sxh=[]
for i in range(100,1000):
    m = list(str(i))
    print(m)
    sum = 0
    for n in m:
        sum+=int(n)**3
    if sum == i :
        sxh.append(i)
print(sxh)

# 用 python 写个冒泡排序
a = [1, 3, 10, 9, 21, 35, 4, 6]
# 冒泡排序是对每一个数进行比较，从第一个数开始要比较len(a)-1，len(a)-2,...,1
# 先定义一个每个数要比较的次数的数列
s = list(range(1,len(a)))[::-1]
print(s)
for i in s:
    for j in range(i):
        if a[j]>a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
    print("第{}轮进行替换数据".format(len(s)-i+1))
print(a)

# 斐波那契数列
# 已知一个数列：1、1、2、3、5、8、13、。。。。的规律为从 3 开始的每一项都
# 等于其前两项的和，这是斐波那契数列。求满足规律的 100 以内的所以数据
a = 0
b = 1
while b < 100:
 print(b, end=",")
 a, b = b, a+b


 # 查看端口是否占用   netstat -anp 端口号
 # 查看已占用端口 netstat - nultp
 # 查找根目录下文件 find / -name 文件名 locate 文件名
 # 查找某个路径下文件   find /bin -name 文件名
 # 模糊查找路径下包含'str'的文件 find /bin -name 'str'
 # 当前目录下查找文件名'str'开头的文件  find . -name 'str'
 # 查找小于100k的文件  find / -size -100k