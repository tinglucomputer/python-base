date_list = ["10月{}日".format(i) for i in range(1, 10)]  # 使用列表推导式+格式化生成一个日期的列表

len(date_list)  # 表明列表的长度

# print(date_list)

name_list = ["dongtinglu", "张三", "dongtinglu"]

name_list.append("wangwu")  # 增加

name_list.insert(1, "找死")  # 向列表中在指定位置增加指定元素

print(name_list.count("dongtinglu"))    # count()函数统计数据在列表中出现的次数

name_list.remove("dongtinglu")  # remove需要遍历列表找到第一次出现的值删除

# print(name_list)

name_list.pop(1)    # pop删除指定位置的元素

del name_list[0]    # del关键字可以删除列表指定位置的元素,实质应该是断开引用,与free相似

temp_list = ["沙师弟"]

name_list.extend(temp_list)  # 把另外一个列表链接到当前列表的尾部做扩展

name_list.sort()    # 升序

name_list.sort(reverse=True)    # 降序

name_list.reverse()     # 反转列表

# print(name_list)

single_list = [5]  # 列表没有单元素非列表现象

single_list.index(5)    # 取索引

single_list.clear()  # 清空列表

# print(type(single_list))

