# a = input("输入一行，代表要计算的字符串，非空，长度小于5000:")
# b = a.split(' ')
# print(len(b[len(b)-1]))

# def jisuan(a):
#     l = 0
#     r = len(a)-1
#     i = l
#     j = r
#     v = 0
#     while i < j:
#         if a[l] < a[r]:
#            if a[l] > a[i+1]:
#                v += a[l]  - a[i+1]
#                i += 1
#            else:
#                 l = i+1
#                 i = i+1
#         else:
#             if a[j] > a[r-1]:
#                 v += a[j] - a[r-1]
#                 r -= 1
#             else:
#                 j = r-1
#                 r = r-1
#     return v
# a = [3,1,2,5,2,4]
# print(jisuan(a))




# while True:
#     try:
#         a=input("输入字符串")
#         b=[]
#         c=''
#         for i in range(len(a)):
#             b.append(a.count(a[i]))
#         for i in range(len(a)):
#             if min(b)!=b[i]:
#                 c=c+a[i]
#         print(c)
#     except:
#         break

class Count:
    def count(self):
        a = input("请输入字符串：").lower()
        b = input("请输入字符：").lower()
        li = list(a)
        coun = 0
        for i in li:
            if b == i:
                coun += 1
        print(coun)

if __name__ == '__main__':
    Count().count()
