str1 = "hollo python"
#统计字符串长度
print(len(str1))
# 统计某个字符串出现的字符,若不存在得到 0 的结果
print(str1.count("o"))
# 某一个字符串出现的位置
print(str1.index("lo"))
#子字符串不存在会报错
print(str1.index("no"))