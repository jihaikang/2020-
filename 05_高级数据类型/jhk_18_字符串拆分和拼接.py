# 将字符中的所有字符删掉
# 在使用" "作为分隔符，拼接成一个整齐的字符串
poem_str ="\t\n登鹳雀楼 \t王之涣\t\n 白日依山尽 \t黄河入海流 \t欲求千里目 \n更上一层楼"


print(poem_str)
# 拆分字符,使其成为列表
poem_splist =poem_str.split()
print(poem_splist)
# 合并字符串，返回字符串
result = print(" ".join(poem_splist))