# 假设以下内容是从往上爬取下来的
#  要求：顺序并且居中对齐输出文本
poem = ["\t\n登鹳雀楼",
        "王之涣",
        "白日依山尽",
        "黄河入海流",
        "欲求千里目",
        "更上一层楼\t\n"]
print(poem)
for poem_str in poem:
    print("|%s|" % poem_str.strip().rjust(10))
print(poem)

