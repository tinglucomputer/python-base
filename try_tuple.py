info_tuple = ("dongtinglu", 24)

sing_tuple = ("dong", )  # 元组在只有一个元素时,不加逗号,系统不会把这个变量看成是元组

sing_tuple.index("dong")    # 取索引

sing_tuple.count("dong")    # 计数

print("%s 的年龄是 %d" % info_tuple)    # 元组内的参数和格式化字符串里的参数类型、个数一致

