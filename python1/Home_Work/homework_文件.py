"""
1.编写如下程序
创建一个txt文本文件，来添加数据
a.第一行添加如下内容：
name,age,gender,hobby,motto

b.从第二行开始，每行添加具体的用户信息，例如：
yuz,17,男,假正经,I am yours
cainiao,18,女,看书,Lemon is best!

c.具体用户信息要求来自于一个嵌套字典的列表（可自定义这个列表），例如：
person_info = [{"name":"yuz","age":"18","gender":"男","hobby":"","motto":"hehe"}]

d.将所有用户信息写入到txt文件中之后，然后再读出

"""
person_info = [{"name":"yuz","age":"17","gender":"男","hobby":"假正经","motto":"I am yours"},
               {"name":"cainiao","age":"18","gender":"女","hobby":"看书","motto":"Lemon is best!"}]

def get_value_lines(info):
    """获取每一行的数据
    列表转化成行的字符串形式
    [{},{}] ==> name,yuz
    """
    lines = ''
    for person in info:
        line = []
        for e in person.values():
            line.append(str(e))
        # 列表转化成字符串
        line_str = ','.join(line)+'\n'
        lines += line_str


def main():
    """主题逻辑"""
    title = person_info[0].keys()
    with open('info.txt','w+') as f:
        f.write('name,age,gender,hobby,motto\n')  #byte
    data = get_value_lines(person_info)
    with open('info.txt','w+'):
        f.write(data)
    with open('info.txt','a',encoding = 'utf-8') as f:
        f.write(data)
    with open('info.txt','r',encoding='utf-8' ) as f:
        print(f.read())
        