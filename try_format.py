# 本程序显示了字符串的格式化

print("{} {} {}".format("dong", "ting", "lu"))

print("{1} {0} {2}".format("ting", "dong", "lu"))

# 使用字典格式化
person = {"age": 20, "name": "dongtinglu"}

print("I am {name}, {age} years old.".format(**person))

# 使用列表格式化
stu = [["dongtinglu", 20], ["liwenfei", 21]]

print("I am {0[0][0]}, {0[1][0]} years old. {0[1][0]} is my friend, {0[1][1]} years old.".format(stu))


# 一个*代表tuple,直接参数
def m(*p):
    print(p)


m(1, 2, 3)


# 两个*代表字典,要有关键字参数
def m1(**p):
    print(p)


m1(x=1, y=2, z=3)

# 三元运算符
a = 2 if 4 > 3 else 3

