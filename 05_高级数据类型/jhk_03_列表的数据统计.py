name_list = ["张三","李四","王五","张三"]
list_len = len(name_list)
#len函数统计列表元素的数量
print("列表中有%d个元素" % list_len)
count = name_list.count("张三")
print("张三出现了%d次" % count)
name_list.remove("张三")
print(name_list)
