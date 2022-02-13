# 变量定义以后一定要赋值
age = 18    # 数字 整数
# 字符串数据的左右两边必须叫引号
# 单引号、双引号
name = "tan mh"
name_two = "jaychou"
# 三引号可以打印多行
name_three = """胡歌,
林俊杰,
周杰伦
"""
print(name_three)
name_four = '"小时候"很帅"'
print(name_four)
# 如果字符串内部有双引号，name就用单引号表示字符串
# 如果内部有单引号，外面就用双引号
# 单引号双引号只能写一行
name_five = '"小时候"很帅'
print(name_five)


# TODO：如果想用字符串表示windows系统下面的路径，
#  在字符串前面加一个r'D:\test\',遇到反斜杠进行转义
file_path = r'd:\huge\test.xls'
print(file_path)

