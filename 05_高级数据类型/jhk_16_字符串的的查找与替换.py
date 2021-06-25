hollo_str = "hollo world"

# 判断是否以指定的字符串开始
print(hollo_str.startswith("hollo"))

#判断是否以指定字符串结束
print(hollo_str.endswith("world"))
#查找指定字符串会返回-
# index同样可以查找指定字符串的索引
# index指定字符串不存在，会报错，而find返回-1
print(hollo_str.find("llo"))
print(hollo_str.find("abc"))

# 替换字符串
print(hollo_str.replace("world","python"))
# replace 执行完成之后返回一个新的字符串
# 注意不会修改原有字符串
print(hollo_str)


