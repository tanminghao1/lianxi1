# 字符串拼接，加号拼接
name_one = 'bad'
name_two = 'boy'
name_full = name_one + ' ' +name_two
print(name_full)

# 字符重复多次
name1 = 'badboy'
print((name1+' ') * 5)

# 获取字符串当中的某一个字符
# 判断字符串的长度len()
name_three = '你好 再见'
print(len(name_three))
# name = []  列表
# 如果想获取其中的某一个字符使用索引,字符串是有序的
# name_three[],索引，是获取某一个字符
# TODO：获取数据索引是从0开始
name_four = name_three[0]
print(name_four)


# 如果从左边开始数，就是0开始1,2
# 如果你从右边开始数，就是-1，-2，-3
name_five = name_three[-1]
print(name_five)

# TODO：切片，如果获取多个字符
name = '雨泽最帅，绝对的'
print(name[1])
# TODO：切片用法：name[start:end:step]，step默认为1
# 取左边不取右边，0《= X 《=step
print(name[0:2])
print('我想获取'+ name[0:4])
# 省略右边的，取剩下的全部
print(name[0:])
# 省略左边的，取左边全部
print(name[:3])
# 全部省略，获取全部
print(name[:])
# 跳级，步长，step
print('跳级::::', name[::1])
print('跳级::::', name[::2])   # 隔2取1
print('跳级333', name[::3])    # 隔3取1
# TODO:如果切片跳出去了，切片超出，获取剩下的所有数
print(name[1:1000])
print(name[99:1000])     # 起始超出，获取为空
# TODO：如果索引超出范围，会报IndexErro
# print(name[1000])