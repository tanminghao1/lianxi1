class Demo:
    member_id = 2
    token = 'abc'

if __name__ == '__main__':
    Demo.member_id = 3
    # 不存在属性，获取会报错
    # print(Demo.memer_id)
    # 不想报错
    a = getattr(Demo,'memer_id','闲人')
    print(a)