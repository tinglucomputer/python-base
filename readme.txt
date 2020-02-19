python基础语法教程
基本数据类型 整数 浮点型 字符串 布尔值
字符串 列表 元组属于序列
设置字体和颜色 File->Settings->Appearance/Editor->font
元组使用()来定义 相当于只读列表
列表使用[]来定义 是最常用的一种数据类型 可以写列表
词典使用{}来定义 是一个map结构访问时是用Key来访问Value并不是靠索引
数据、字符串、元组是不可修改的,列表和字典是可以修改
列表使用中括号[]定义的,元组是用圆括号()定义的,而且对于元组来说不可增加和删除 列表可以 故列表的操作要方便的多
序列中存在一些基本的操作：object1 [in (not in)] [+连接操作] [*表示重复] [切片操作] object2
选中方法名,点击ctrl+q会出现关于该函数的完整表述
1.列表
    经常使用的场景:存储相同类型的元素,使用循环对每一个元素做相同的操作
2.元组
    经常使用的场景:
        函数的参数或者是返回值可以是任意多个
            返回多个参数:return (var1, var2)或者不带括号
            实参是任意个:*args可以接收一个元组,**kwargs可以接收一个字典
        格式字符串,格式化字符串后面的()本质是昂就是一个元组
        让列表不可修改,保护数据安全 list(tuple) tuple(list)
3.字典
    字典是无序的结合,列表和元组是有序的,故不能使用索引获取字典中的元素
    是键值对的形式
        key是键,是索引,具有唯一性,只能是字符串、数字、元组
        value是值,可以是任意的数据类型
    经常使用的场景:
        使用键值对描述一个物体的相关信息
        将多个字典组合成一个列表
4.字符串
    1.判断类型
        string.isspace():不仅仅可以判断空格,也可以判断\t\n\r等空白字符
            [注]\r回车表示回到该行的最开始位置,\n表示换行,
            windows系统下\n就表示换行到下一行的首位置,linux系统中\r\n才表示换行到下一行的首位置
        string.isalpha():判断字符串是否是一个字母串
        string.isalnum():判断字符串是否是一个字母数字串
        string.isdecimal():判断字符串是否一个整数的数字串,常用
        string.isdigit():
        string.isnumeric():
        string.istitle():判断字符串每一个单词的首字母是否大写,像一个标题一样
        string.islower():
        string.isupper():
    2.替换和查找
        string.startswith(str):判断字符串是否以str开头
        string.endswith(str):判断字符串是否以str结尾
        string.find(str,start=0,end=len(string)):判断字符串中是否包含了str,如果不指定start和end参数则在全串中查找,如果指定了则在范围内查找,但是end是取不到的
           如果找到了则返回str在字符串中出现的位置,如果没有找到则返回-1
        string.rfind(str,start=0,end=len(string)):类似于find()函数,只不过从右侧开始匹配,如果出现过多次只返回第一次出现的位置
        string.index(str,start=0,end=len(string)):获取字符串中出现str的位置
        string.rindex(str,start=0,end=len(string)):类似于index()函数,只不过从右侧开始查找
        string.replace(old_str,new_str,num=string.count(old_str)):替换函数,如果不指定替换次数则说明全部替换,一般也是全部替换
    3.大小写转换
        string.capitalize():第一个字符大写
        string.title():标题化
        string.lower():
        string.upper():
        string.swapcase():翻转string的大小写
    4.文本对齐
        string.ljust(width,fillchar):左对齐,width长度,fillchar填充字符
        string.rjust(width,fillchar):右对齐
        string.center(width,fillchar):居中
    5.去除空白字符
        string.lstrip():
        string.rstrip():
        string.strip():
    6.拆分和拼接
        string.split(seq,num):以seq为分隔符拆分string,如果不指定seq则以任何空白字符或串作为分隔符,结果就是字符串中没有空白字符,拆分结果是列表
        seq.join(sequence):按seq分隔符组合sequence序列,返回结果是一个大字符串
    7.切片
        数据切片对字符串、元组、列表都有用
        string[startIndex:endIndex:step]:切片不包含endIndex处的字符,
            startIndex:不指定表示从开始切
            endIndex:不指定表示一直切到最后,可以切最后一个元素
            step:可以连续切片,也可以在startIndex上偏移切片,如果是正数表示正序切片,如果是负数表示倒序切片,结果也是倒序的
5.一些常用的操作
    1.in/not in:用于判断包含或者不包含成员,用于字典时主要判断key
    2.完整的for循环:content2只有当遍历完set中所有的对象时才会被执行到,如果在content1中有一个break语句退出了,并不会被执行到
        for var in set:
            content1
        else:
            content2
    3.+=
        对字符串和数字执行该操作时,先相加后赋值,变量的引用会改变,原有引用的数据并不会改变
        但是对于列表进行该操作时,相当于调用extend()方法,那么变量的引用不会变,原有数据会改变
    4.元组和字典的拆包
        当自定义函数同时想接收元组和字典参数时,为了避免在实参形式下,封装的元组和字典一块传递给函数时误认为只有元组而没有字典的情况
        def fun(*args, **kwargs):
            content
        var1 = (...)
        var2 = {...}
        # fun(var1, var2)
        fun(*var1, **var2)



