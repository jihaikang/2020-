xiaoming = {"name":"haizi",
            "shenggao":185,
            "age":18,
            "gender": True}
#统计键值对数量
print(len(xiaoming))
#合并字典
xiaoming_dict = {'xiaomei':167}
xiaoming.update(xiaoming_dict)
print(xiaoming)
#清空字典
xiaoming.clear()
print(xiaoming)
