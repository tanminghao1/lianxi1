# 1.读取整个文件
# 使用关键词with后不再需要访问文件后将其关闭，python会在合适的时候将其自动关闭
# 查找当前.py文件所属目录下的pi_digits.txt文件
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
# 通过rstrip()删除字符串末尾的空白
print(contents.rstrip())

# 2.文件路径：有时需要打开不在执行文件所属目录中的文件，提供文件路径查找特定位置下文件
# 1>相对路径：执行文件.py所在文件夹下还有其他文件夹
with open('xianren/xianren.txt',mode = 'r',encoding='utf-8') as file_object:
    contents = file_object.read()
print(contents)