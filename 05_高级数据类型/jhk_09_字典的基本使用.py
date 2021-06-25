xiaoming_dict = {"name":"xiaoming"}

#取值
print(xiaoming_dict["name"])
#增加/修改
#如果key不存在，则增加
#如果key存在，则替换
xiaoming_dict ["age"] = 18
print(xiaoming_dict)
#  xiaoming_dict["name"]= "小明"
# print(xiaoming_dict)
#删除
#如果key不存在，则报错
xiaoming_dict.clear()
print(xiaoming_dict)