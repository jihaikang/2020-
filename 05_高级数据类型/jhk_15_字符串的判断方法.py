# 判断空白字符
space_str = " \t\n\r"
print(space_str.isspace())
# 判断字符串中是否包含数字
num_str = "1"
print(num_str)
# 1> 不能判断小数
# 2>unicode 字符串 "(1)"
# 3>num_str="\u00b2"
# 4>中文数字
print(num_str.isdigit())
print(num_str.isdecimal())
print(num_str.isnumeric())
print("sa\'\tbi")
print('hello\tkitty')