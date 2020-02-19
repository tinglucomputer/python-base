person_dict = {"name": "dongtinglu"}

print(person_dict["name"])  # 通过key取值

person_dict["age"] = 18  # 如果字典中没有该键值对则添加,如果有则修改

person_dict.pop("name")  # 删除一个键值对

temp_dict = {"height": 1.78}

person_dict.update(temp_dict)   # 合并字典,如果有相同的键则以temp_dict中的键值对为结果

print(person_dict)

for i in person_dict.items():   # 遍历字典,items()函数得到所有的键值对,每个键值对都是一个元组
    print(i)



