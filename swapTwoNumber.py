# 本程序实现两个数的交换操作
# 在函数内部对形参的赋值操作并不会对实参产生影响


def swap(a, b):

    return b, a


a = 1

b = "dong"

c = [1, 2, 3]

print(id(a), id(b), id(c))

# a, b = swap(a, b)

# print(a, b)

# print(id(a), id(b))

a += 1

b += "dong"

c += [4]

print(id(a), id(b), id(c))