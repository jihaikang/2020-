name_list = ["zhangsan","lisi","wangwu"]
# """
# 1.取值和索引
#list index out of range--列表索引超出范围
print(name_list[2])
#想确定数据的位置
print(name_list.index("lisi"))
# 2.修改
name_list[1] = "李四"
# 3.删除 remove 可以从列表中删除指定的数据
#name_list.remove("wangwu")
#name_list.pop(1) 删除元素的索引
# name_list.clear() 清空列表
# 4.增加
# append,insert,extend
name_list.append("王小二")
name_list.insert(1,"小美眉")
temp_list = ["孙悟空","猪八戒","沙悟净"]
name_list.extend(temp_list)
# """
print(name_list)