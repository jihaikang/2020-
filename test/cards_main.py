import cards_tool


def deal_card(find_dict):
    """操作搜索到的名片字典

    :param find_dict:找到的名片字典
    """
    print(find_dict)

    action_str = input("请选择要执行的操作 "
                       "[1] 修改 [2] 删除 [0] 返回上级菜单")

    if action == "1":
        print("修改")
    elif action == "2":
        print("删除")


while True:
    #Todd(茫茫狐)名片管理系统
    cards_tool.show()
    action = input("请选择使用的功能：")
    print("你的操作是%s" %action)

    if action == '1':
        cards_tool.new_card()
    elif action == '2':
        cards_tool.show_all()
    elif action == '3':
        cards_tool.seach_card()

    elif action =='0':
        cards_tool.show()
        print("欢迎再次使用名片管理系统")
        break
    else:
        print("输入错误,请重新输入：")

