# 定义变量
rusult =0
i = 0
while i <= 6:
    if i % 2 == 0:# 得出偶数
        rusult += i
    i += 1
print("相加偶数结果 %d" % rusult)