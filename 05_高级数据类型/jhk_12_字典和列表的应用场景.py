# 使用多个键值对存储描述一个物体的相关信息，描述更复杂的数据信息
# 将多个字典 放在亿个遍历中，在进行输出
# card_list =(
#     {"name":"haizi",
#      "shenggao": 185,
#      "age": 18,},
#     {"gender": True}
#     ,2,1)
card_list =(1,2,3)
for card_info in card_list:
     print(card_info)
info_tuple = (1,1.85 ,75)
for my_think in info_tuple:
    print(info_tuple)# 同样输出元组遍历情况却不同，编辑器的问题么