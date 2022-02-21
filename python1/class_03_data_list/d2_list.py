# 列表，存储很多数据
# 变量，存储数据
dalao = '小风'
# 列表里面可以存储不同数据类型数据
dalaos = ['小风','K','萌萌哒',3,['钻石','包包','口红','零食']]
# 如果想取出其中的某个元素，通过索引获取
# 和字符串类似
print(dalaos[2])
# TODO:列表的切片使用方法与字符串一致
# 取多个值，使用切片，取左不取右
print(dalaos[2:3])
# 未指定第一个索引，从起始开始
print(dalaos[:3])
# 取到列表末尾最后
print(dalaos[2:])
# 通过负号从末尾开始往前取
print(dalaos[-1:-3:-1])
# 通过负号取最后3位
print(dalaos[-3:])
# 获取列表所有值,将列表复制给其他变量
print(dalaos[:])
dal = dalaos[:]
print()
# 如果子元素当中是列表，继续通过索引获取
print(dalaos[-1][0:2])
# 获取列表长度
print(len(dalaos))
# 字符串不能被修改，只能重新赋值
# 列表可以被修改，可变数据类型
# TODO:坑
dalaos2 = ['随风']
# 添加新的元素 .append() 一次只能添加一个，添加到最后
new_dalao = dalaos2.append('而飘')
print(dalaos2)
# append() 返回这个None
print(new_dalao)
# TODO:坑2
# new_dalao = dalaos2.append('1').append('2')
# print(new_dalao)
# 添加多个元素 .extend([]) 添加多个在最后
dalaos2.extend(['一光','木木','王可爱','美雪'])
print(dalaos2)
# 往指定位置添加 .insert 添加一个元素
dalaos2.insert(0,'小雪')
print(dalaos2)
dalaos2.insert(2,'丢妹')
print(dalaos2)
# 删除元素
# 1.删除指定的值  remove()
dalaos2.remove('丢妹')
print(dalaos2)
# 2.删除指定的索引,pop(提取指定索引值)
xiaoxue = dalaos2.pop(0)
dalaos2.pop(0)
print(dalaos2)
print(xiaoxue)
# pop()没有参数时默认最后一个
dalaos2.pop()
print(dalaos2)
# 3.删除所有元素
# dalaos2.clear()
# print(dalaos2)
# 4.不要去用del,从内存当中直接清除，物理删除
del dalaos2[0]
print(dalaos2)
# 修改
dalaos2[2] = '美雪'
print(dalaos2)
# 5.列表函数
# index  获取索引
print(dalaos2.index('木木'))
# count 统计列表中有多少个‘xx’
print('\ncount函数：',dalaos2.count('美雪'))
# reverse  逆序
dalaos2.reverse()
print(dalaos2)
# 逆序2 重新创造新的变量
new_dalao = dalaos2[::-1]
print(dalaos2)
# 排序
dalaos2 = ['c','b','z','h']
dalaos2.sort()
print(dalaos2)
# 数字排序
dalaos2 = [1,5,7,9,3]
dalaos2.sort()
print(dalaos2)
# 倒序
dalaos2.sort(reverse=True)
print(dalaos2)

# 列表基础操作
countries = ["china","french","american","feizhou","englen"]
print("想去的国家有：",countries)
print("使用函数sortend()排序，不改变原列表排序，打印出：",sorted(countries))
print("使用sortend()后，核实列表顺序",countries)
print("使用sortend(),按字母倒序打印，并不改变原列表：",sorted(countries,reverse=True))
print(f"再次核对列表未被修改：{countries}")
# 将列表逆序
countries.reverse()
print(f"确认列表修改为逆序：{countries}")
# 再次使用逆序，恢复列表
countries.reverse()
print(f"再次使用reverse()恢复列表原顺序{countries}")
print(f"使用方法sort()修改列表按字母顺序排列：{countries.sort()}")
print(f"核对列表按字母顺序排列：{countries}")
print(f"使用方法sort()使列表按字母倒序排列：{countries.sort(reverse=True)}")
print(f"使用sort()后列表按字母倒序排列：{countries}")
print(f"我想去的国家有{len(countries)}个")

# 遍历列表
magics = ["alis","david","bob"]
print("遍历列表：")
for magic in magics:
    print(magic)

# 在for循环中执行更多操作
for magic in magics:
    print(f"{magic.title()}的表演很棒")
print("感谢每位魔术师的表演")

# 创建数值列表
# 使用range(x,y)，获取x到y(不含y)的自然数,只有一个参数时range(y)从0开始取
numbers_1 =list(range(1,6))
print("使\n用range()创建数字列表：",numbers_1)

# 使用range时可以指定步长，创建列表
numbers_2 = list(range(0,10,2))
print("\n取10以内间隔为2的值创建列表：",numbers_2)

# 使用函数range()几乎能创建任何需要的
values = []
for value in range(0,5):
    values.append(value)
print(values)

# 创建1-10的平方和
squares = []
for num in range(1,11):
    # squar = num ** 2
    # squares.append(squar)
    # 可将值直接添加到列表
    squares.append(num**2)
print(f'\n打印1-10的平方数列：{squares}')

# 对数列进行简单的统计计算
digits = [1,2,3,4,5,6,7,8,9,10]
# 统计列表中最小值，最大值，和的函数
print(f'输出列表中最小的值：{min(digits)}')
print(f'输出列表中最大的值：{max(digits)}')
print(f'输出列表所有值的和：{sum(digits)}')

# TODO:生成列表更简洁的方法：列表解析，阅读他人代码时可能会遇到
# 列表解析：将for循环和创建新元素的代码合并成一行，并自动附加新元素
# 列表名 = [表达式 for循环]，for循环给表达式提供值
squares = [value**2 for value in range(1,11)]
print(f'\n列表解析的方法生成列表：{squares}')

# 遍历切片
print("\n遍历切片前三个值：")
for dalao in dalaos[0:3]:
    print(dalao)

# TODO:变量名相当于存储计算机数据的标签，通过变量名赋值不能把值复制给其他变量生成新的列表
dalao = dalaos
print(f'dalaos：{dalaos}')
print(f'dalao：{dalao}')
print("对'dalaos'添加值")
dalaos.append('周杰伦')
print(f'dalao的值仍然指向dalaos：{dalao}')
# 通过切片方式将值复制给其他变量生成一个新的变量
dalao = dalaos[:]
print(f'\ndalaos：{dalaos}')
print(f'dalao：{dalao}')
print("对'dalaos'添加值：林俊杰")
dalaos.append('林俊杰')
print(f'dalao为一个新的列表：{dalao}')
print('dalaos：',dalaos)