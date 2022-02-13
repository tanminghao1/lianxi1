
# 使用制表符或换行符来添加空白
# 使用制表符 \t
print("Python")
print("\tPython")

# 使用换行符 \n
print("Languages:python java c c++")
print("Languages:\npython \njava \nc \nc++")

# 同时使用\t\n
print("Languages:\n\tpython\n\tjava\n\tc\n\tc++")

# 删除字符串空白
favorite_language  = " python "
# 删除右边空格
print(favorite_language.rstrip())
# 删除左边空格
print(favorite_language.lstrip())
# 删除左右两边空格
print(favorite_language.strip())
