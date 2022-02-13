# 集合不是键值对
# 集合是无序的
# 能通过索引获取元素吗？
# TODO:重复的元素丢掉，集合用的最多是去重
set_yuz = {"yuz","xixi","gg",'gg'}
print(set_yuz)
print(len(set_yuz))
# 去重
# 类型转换，列表-》集合-》列表
set_yuz = list(set(["yuz","xixi","gg",'gg']))
print(f'列表yuz:{set_yuz}')
set_yuz2 = set(set_yuz)
print(f'集合yuz2:{set_yuz2}')
print(f'列表yuz:{set_yuz}')
# 列表
# 字典
# 元组，1.一个元素的元组必须要加逗号 2.元组的不可变性和列表的可变性
# 集合set,1.主要是去重 2.无序

# split
a = 'hello word xixi'
print(a.split(' '))
print(a.split(' ',1))