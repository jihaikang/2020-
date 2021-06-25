import jhk_04_函数
import keyword

jhk_04_函数.print_line('-',10)
jhk_04_函数.print_lines('+',4)
print(jhk_04_函数.name)
print(keyword.kwlist)
print(len(keyword.kwlist))
card_list = {"name": "张三",
              "qq": "12345",
              "phone": "110"}
for k in card_list:
    print("%s %s" % (k, card_list[k]))



