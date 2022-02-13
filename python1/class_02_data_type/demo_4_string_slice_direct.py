name = '不懂，是一位超级大佬'
print(name[3:6:1])

# 从右往左
print('获取佬大:' + name[-1:-3:-1])   # 右边不包含，+1
#  从右往左，佬大...步长如果为正，从左往右，如果为负数，从右往左数
print(name[-1:-3:1])   # 最后一位-1到-3往左边，step右边数，取不到值
print(name[-3:-1:1])
print(name[4:1:-1])

# 倒序排列
# 未取到0位
name2 = name[-1:0:-1]
print(name2)
print(name[-1:0:-1])  #未取到0位
# 取到0位
print(name[-1::-1])
print(name[::-1]) #倒序取所有
print(name[2:0:-1])
print(name[1:2:1])
print(name[::])