tuple_demo = ()
print(tuple_demo)
# TODO:一个元素的元组表示不是一个元组，而是去掉括号以后的原始数据类型
tuple_demo_2 = (1)
tuple_demo_3 = 1
print(tuple_demo_2)
print(tuple_demo_3)
# 如果想表示一个元素的元组，在元素后加逗号
tuple_demo_4 = (1,)
print(tuple_demo_4)

# 元组解包
# 变量名和值一一对应
family,name = ('wang','yuz')
print(family)
print(name)
a,b = 3,4
print(a)
print(b)
# 多的值都给other
family,name,*other = ('wang','yuz','hello','word')
print(other)