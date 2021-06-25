card_list = []
def show():
    """
    显示菜单
    :return:
    """
    print('-'*50)
    print('欢迎使用【菜单管理系统】V1.0')
    print('')
    print('1,新建名片')
    print('2,显示全部')
    print('3,查询名片')
    print('')
    print('0,退出系统')
    print('')
    print('*'*50)
def new_card():
    """
    新建名片
    :return:
    """
    print('-'*50)
    print('功能:新建名片')
    # 提示用户输入名片信息
    name = input("请输入姓名:")
    phone = input('请输入电话:')
    qq = input('请输入QQ账号:')
    email = input('请输入邮箱:')
    card_dict = {"name":name,# 将用户信息保存到字典里
                 "phone":phone,
                 "qq":qq,
                 "email":email}
    card_list.append(card_dict) #将用户字典添加到名片列表
    print(card_list)
    print("成功添加%s 的名片" % card_dict['name'])
    return
def show_all():
    """
    显示所有名片
    :return:
    """
    print('-'*50)
    print('功能:显示全部')
    # 打印表头
    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t\t")

    print("")

    # 打印分隔线
    print("=" * 50)

    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                        card_dict["phone"],
                                        card_dict["qq"],
                                        card_dict["email"]))
    if len(card_list) == 0:
        print("提示：没有任何名片记录")

        return

def seach_card():
    '''
    搜索名片
    :return:
    '''
    print('-'*50)
    print('功能:搜索名片')
    # 提示要搜索的名字
    find_name = input('请输入查找的姓名:')
    for card_dict in card_list:
        if card_dict['name'] == find_name:
            print('姓名/t/t电话/t/tqq/t/t邮箱')
            print('-'*50)
            print('%s/t/t%s/t/t%s/t/t%s' % (card_dict['name'],
                                            card_dict['phone'],
                                            card_dict['qq'],
                                            card_dict['email']))

            print('-' * 50)
            break
    else:
        print('没有找到%s'%find_name)



