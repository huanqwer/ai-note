print("hello world")

# 格式化输出练习
int1 = 10
float1 = 3.14159
str3 = f"{int1 = }, {float1 = }"
print(str3)

# 分支语句练习
from random import randint

balance = randint(0, 100)
price = 50
print(f"余额: {balance}")
# 比较价格和余额
if balance  < price:
    print("余额不足，请充值")
print("欢迎下次光临")

# 简单语句组
var = 100
if (var == 100) : print("变量var的值为100")
print("Good Bye!")

# 多分支 - 判断人生处于哪个阶段
from random import randint

print("此人年龄为", age := randint(0, 100))
if age < 2:
    print("婴儿")
elif age < 4:
    print("幼儿")
elif age < 13:
    print("儿童")
elif age < 20:
    print("青少年")
elif age < 65:
    print("成年人")
else:
    print("老年人")

"""
给定一个三位状态码
左边第一位表示大小写状态（1 - 大写，0 - 小写）
第二位标识输入法语言（1 - 简体中文， 0 - 英语）
第三位表示输入法模式（1 - 中文，0英文）
"""
state = 0b011
# 判断是否为大写状态
if state & 0b100 == 0b100:
    print("大写状态")
else:
    # 不是大写状态
    # 判断是否为“简体中文 - 微软拼音”
    if state & 0b010 == 0b010:
        if state & 0b001 == 0b001:
            print("微软拼音 - 中文")
        else:
            print("微软拼音 - 英文")
    else:
        print("英文输入法")


"""
给定月份，求该月有多少天
"""
match month := 3:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print(f"{month}月有31天")
    case 4 | 6 | 9 | 11:
        print(f"{month}月有30天")
    case 2:
        print(f"{month}月有28天")
    case _:
        print(f"{month}月有?天")

"""
使用if来获取两个数中较大的一个
"""        
num1 = 2
num2 = 3
max_num = num1 if num1 > num2 else num2
print(f"较大的数是: {max_num}")

"""
第一周有两只兔子，
此后每周兔子数量都为上周的两倍，
期间没有兔子死亡，求第10周有多少只兔子
"""
rabbit = 2
week = 1
while week < 10:
    rabbit = rabbit + rabbit * 2
    week += 1
    print(f"第{week}周有{rabbit}只兔子")

"""
打印进度条
"""
import time

num = 1
while num <= 100:
    print(f"\r进度: {num}%", end="")
    time.sleep(0.1)
    num += 1