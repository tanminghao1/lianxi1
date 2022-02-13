"""
正则表达式是一种通用的字符串匹配技术，是不会因为编程语言不一样而发生变化的
想要查找某种特征的，具有一定规则的字符串，都是可以尝试使用正则表达式
jsonpath，xpath，解析相关

匹配的方式：只是python当中的封装，re
-match
-search
-findall

discover

* 匹配0次或者任意次
+ 匹配1次或者任意次
. 匹配任意字符（除了\n）
\w 匹配字母、数字、下划线
\d 匹配数字
？ 匹配0次或者1次 非贪婪模式
[]匹配里面的任意一个字符
{m,n}至少，最多，多少次

"""

# 匹配特定的字符串 “abc”
import re
# re_pattern = r'abc'
# 在带有 ‘r’ 前缀的字符串字面值中，反斜杠不必做任何特殊处理。
# 从“wofowpqfowfjowefjiwoefabcowof” 这个字符串当中匹配是否有 re_pattern
# match 表示：从开始的位置进行匹配
# res = re.match(re_pattern,"wofowpqfowfjowefjiwoefabcowof")
# print(res)

# search,全文匹配
# res = re.search(re_pattern,'wofowpqfowfjowefjiwoefabcowof')
# print(res.group())
# 返回值都是一个 匹配对象Match ，需要通过match.group() 获取匹配值
# findall,全部匹配
# res = re.findall(re_pattern,"wofowpqfowfjowefjiwoefabcowof")
# print(res)

# [abc],中括号表示匹配每一个字符
# re_pattern = r'[abc]'
# res = re.findall(re_pattern,"wofowpqfowfjowefjiwoefabcowof")
# print(res)

# re_pattern = r'{a}'
# res = re.findall(re_pattern,"wofowpqfowfjowefjiwoefabcowof")
# print(res)
# '.'是表示匹配任意一个字符,除了\n换行符
# re_pattern = r'.'
# res = re.findall(re_pattern,"wofowpqfowfjowefjiwoefabcowof")
# print(res)

# \d 表示匹配一个数字字符，等价于[0-9]
# \D 表示匹配非数字

# \w 表示匹配任意数字、字母、下划线
# re_pattern = r'\w'
# res = re.findall(re_pattern,"wofo11wpqfowfj22owefji33woefabcowof")
# print(res)

# \s 表示匹配任何空白字符，包括空格，制表符，换页符等

# # {2}，大括号表示匹配任意字符长度，搭配匹配规则使用,{2,}加逗号表示最少匹配次数,python中默认为贪婪模式，会匹配尽可能长的字符串
# re_pattern = r'\w{2,}'
# res = re.findall(re_pattern,"wo@_fo11wp&qfowfj22owefji33woefabcowof")
# print(res)

# 如何去匹配一个手机号码
# re_pattern = r'1[3574]\d{9}'
# res = re.findall(re_pattern,"wofo11wp17673054644qfowfj22owefji33woefabcowof")
# print(res)

# # *表示匹配0次或者任意次，通配符
# re_pattern = r'\d*?'
# res = re.findall(re_pattern,"wofo11wp17673054644qfowfj22owefji33woefabcowof")
# print(res)

# +表示至少匹配一次
# re_pattern = r'\d+'
# res = re.findall(re_pattern,"wofo11wp17673054644qfowfj22owefji33woefabcowof")
# print(res)

# .表示匹配任意字符
# re_pattern = r'\d.'
# res = re.findall(re_pattern,"wofo11wp17673054644qfowfj22owefji33woefabcowof")
# print(res)

# ？表示匹配0次或者1次，可以表示非贪婪模式
# re_pattern = r'\d*?'
# res = re.findall(re_pattern,"wofo11wp17673054644qfowfj22owefji33woefabcowof")
# print(res)

# ^表示开头匹配  $表示结尾匹配
# re_pattern = r'^\d'
# res = re.findall(re_pattern,"wofo11wp17673054644qfowfj22owefji33woefabcowof3")
# print(res)

# re_pattern = r'\d$'
# res = re.findall(re_pattern,"wofo11wp17673054644qfowfj22owefji33woefabcowof3")
# print(res)

mystr = '{"member_id":"#member_id#","loan_id":#loan_id#,"username":#username#}'
# 匹配规则
# re_pattern = r'#.*?#'
# re_pattern = r'#(.*?)#'   # 不要#，用括号括起
# res = re.findall(re_pattern,mystr)
# print(res)

# 替换 re.sub()替换操作,不加数字，替换所有，加数字，替换几次,每次替换的数据不一样，所以不能一次性替换
# new_str = re.sub(re_pattern,'123',mystr,1)
# mystr = re.sub(re_pattern,'me123',mystr,1)
# mystr = re.sub(re_pattern,'loan123',mystr,1)
# mystr = re.sub(re_pattern,'tokenloan123',mystr,1)
# print(mystr)

class Context:
    member_id = 888
    loan_id =222
    token = '232jijiv2'
    username = 'yuz'

def replace_label(target):
    """用data替换target里的标签
    {"mobile_phone":"*phone*"} ==> {"mobile_phone":"137"}
    """
    """while循环"""
    re_pattern = r'#(.*?)#'
    while re.findall(re_pattern,target):
        # 如果能够匹配,再通过search匹配一次得到要替换的key，进行动态替换
        key = re.search(re_pattern,target).group(1)
        # 使用getattr动态获取属性值，转换为字符串类型替换
        target = re.sub(re_pattern,str(getattr(Context,key)),target,1)
    return target


if __name__ == '__main__':
    print(replace_label(mystr))
