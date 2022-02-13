# 1.删除列表中‘矮穷丑’，写出所有方法
info = ["yuze",18,"男","矮穷丑",["高","富","帅"],True,None,]
# print(info.pop(3))
# print(info.pop(-5))
# print(info)
# info.remove("矮穷丑")
# print(info)
# del info[3]

# 2
# 收取你的个人信息，存储你的：姓名，性别，年龄
me = ['谭铭昊','男','27']
# 需要补齐你的身高和联系方式
# me.append('170')
# me.append('17673054644')
me.append(['170','17673054644'])
print(me)
# me.insert()
# print(me)
me.pop(-1)
print(me)
me.extend([180,18888887777])
# 列表操作方式
lieb = [1,2,3,4,5]
lieb.insert(0,0)
lieb.append(6)
lieb.extend([7,9,8])
print(lieb)
# 排序
lieb.sort()
print(lieb)
lieb.sort(reverse=True)
print(lieb)


