"""
os和open的作用:
自动生成测试报告，创建文件，存放文件夹

如何读取文件
1.打开文件：内置函数 open(),mode默认参数
open(path/文件名称,mode='r'，encoding='utf-8')  默认是读取
2.读取
3.(一定要)关闭文件  ,数据不对，写入内容不生效

mode:
1.'r',读取
2.'w',覆盖原有内容，编写
3.'a',追加内容编写，不会覆盖
4.'b',binary,二进制，图片，视频

1.'rt' 加t,文本模式读取，省略不写
2.'rb',binary,加r,二进制，图片，视频




读取文件根据指定的编码格式读取
编码是根据一定的规则将计算机内容的机器字节码转化成人能看懂的字符
编码，string-->byte
解码，byte-->string


"""
import os
# 获取绝对路径下的文件夹路径及名称
dir_name = os.path.dirname(os.path.abspath(__file__))
# 拼接一个路径
xianren = os.path.join(dir_name,'xianren.txt')
f = open(xianren,encoding='utf-8')
print(f.read())
f.close()

# 'hello'.encode()
# b'hello'.decode()

# # 'w',覆盖文件内容，写入新的内容,mode= 'wt' 省略了t
# f = open(xianren,mode='w',encoding='utf-8')
# f.write('胡哥哥')
# f.close()

# # 'a',追加内容，不会覆盖，mode= 'at'
# f = open(xianren,mode='a',encoding='utf-8')
# print(f.write('小马哥'))
# f.close()

# 'b',binary,二进制，图片，视频
# dir_name = os.path.dirname(os.path.abspath(__file__))
# png_pic = os.path.join(dir_name,'1.jpg')
# print(png_pic)
# f = open(png_pic,mode='rb')
# print(f.read())
# f.close()