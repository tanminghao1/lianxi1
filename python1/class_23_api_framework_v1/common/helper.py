# 自动生成手机号码
import random

def generate_mobile():
    """随机生成一个手机号码。。   1[3,5,8,9] + 9"""
    phone = '1' + random.choice(['3','5','7','8'])
    for i in range(9):
        num = random.randint(1,9)
        phone += str(num)
    return phone

if __name__ == '__main__':
    print(generate_mobile())