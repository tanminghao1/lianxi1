# 变量命名
my_string = "今晚你那里下雪了吗？面对寒冷你怕不怕"
# 获取长度 len()
len(my_string)
# 转化大写 .upper()
my_string = 'snow now'
print(my_string.upper())
# 转化小写 .lower()
print(my_string.upper().lower())
# 大小写互换
new_string = 'Snow beAuty'
print(new_string.swapcase())
# 格式化首字母大写
print(new_string.title())
# 查找，当查找不到的时候，find会返回-1
if_snow = my_string.find('下雪')
print(if_snow)
# TODO:当find找到指定元素时，返回开始的字母的索引值
if_snow = my_string.find('w n')
print(if_snow)
# index 和 find的作用相似
if_snow = my_string.index('w n')
# 不同,找不到时，报错 ValueError
# 昨天讲的错误类型，IndexError(索引错误)
if_snow1 = my_string.index('w n')
print(if_snow1)
# 替换 replace(原值，替换值，替换几个)
dalao_name = '本本'
new_dalao = dalao_name.replace('本','去',1)
print(dalao_name)
print(new_dalao)
# 统计 count()
song = '理想啊，理想，我的理想，永远那么年轻，啊啊啊啊，理想'
print(song.count('理想'))
# TODO:join,字符串拼接，正规方式，代替+号
song_1 = '理想啊理想'
song_2 = '我的理想'
song_3 = '永远那么年轻啊啊啊'
song_total = ('*'.join([song_1,song_2,song_3]))
print(song_total)
# TODO:字符串分割 split()
print("song_total",song_total.split('*'))
# strip 用的多，去掉左右两边指定字符
guniang = ' 心拼命姑娘心 '
print(guniang.strip(' 心'))
# 如果左右两边不一样，左边lstrip，右边rstrip
gunianggg = '男拼命姑娘儿'
print(gunianggg.lstrip('男'))
print(gunianggg.rstrip('儿').lstrip('男'))
print(gunianggg.strip('拼姑'))
# 判断字符串里是否是一个正整数 .isdigit
a = '-2345'
print(a.isdigit())

