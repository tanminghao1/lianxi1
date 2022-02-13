# 元组()：适合用于存储在程序中不需改变的数据集，元组不可以被修改，元组就是不可变的列表
# 列表[]:适合用于存储在程序运行期间可能变化的数据集，列表是可以修改的
dalaos = ["晓峰","一罐","丢妹妹","萌萌哒"]
# 元组形式和列表非常相似，元组用()，列表用[]
dalaos_tuple = ("晓峰","一罐","丢妹妹","萌萌哒")

print(dalaos_tuple)
# 获取某一个元素，索引，和列表一样
print(dalaos_tuple[0])
# 获取多个，切片
print(dalaos_tuple[0:2:1])
# 元组不能添加，修改，删除
# 元组不可变，和字符串类似，只能重新赋值
# 修改的是元组的元素，不支持修改
# dalaos_tuple[1] = '小马哥'
# 元组的不可变性是相对的，不是完全不能变
# 只要看修改的索引前面是不是可变的类型
tuple_yuz = ('yuz','一罐',['闲人','大大'])
tuple_yuz[2][0] = '新列表'
print(tuple_yuz)
tuple_yuz2 = ('yuz','一罐',{'闲人':'大大'})
# 索引前面tuple_yuz2是元组，代表我们修改的是元组元素，不可以
# tuple_yuz2[2] = 'hello'
# tuple_yuz2[2]是字典，可变的，可以修改
tuple_yuz2[2]["name"] = 'hello'
print(tuple_yuz2)
yuz = ['yuz','一罐',('闲人','大大')]
# yuz是列表，可变
yuz[2] = 'hello'
print(yuz[2])
# yuz[2] 是元组，不可变
# yuz[2][1] = 'word'
# print(yuz)


# python基础
# 定义一个元组
dimension = ('200','50')
print(dimension[0])
print(dimension[1])
# 尝试修改元组内的值会报TypeError: 'tuple' object does not support item assignment
# dimension[0] = 1
# 元组有逗号标识，创建只有一个元素的元组，必须在元素后加上逗号
my_t= (1,)

# 遍历元组中的所有值
dimensions = (200,300)
for dimen in dimensions:
    print(f'\n遍历元组元素：{dimen}')

# 修改元组变量，不能修改元组元素，但能给存储元组的变量重新赋值
dimensions1 = (200,300)
print("\n白色衣服尺寸：")
for dimen1 in dimensions1:
    print(dimen1)
dimensions1 = (500,600)
print('黑色衣服尺寸：')
for dimen1 in dimensions1:
    print(dimen1)
# 相比于列表，元组是更简单的数据结构，如果需要存储的一组值在程序的某个生命周期内部不变，就可以使用元组


# 作业
# 1.有一家自助餐厅，只提供五种菜品，请想出五种食品并存储与元组中
foods = ('炒粉','沙拉','肥牛','肥羊','牛排')
# 2.使用一个for循环，将食品都打印出来
print('\n自助餐的菜品有：')
for food in foods:
    print(food)
# 餐馆替换了2种菜品
print('新的菜品为：')
foods = ('炒粉','沙拉','螃蟹','蛋糕','牛排')
for food  in foods:
    print(food)