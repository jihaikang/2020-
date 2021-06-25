def print_line(char,times):

   print(char * times)


def print_lines():
    """打印多行分割线

    :param char: 分割线使用的字符
    :param times:重复的次数
    """
    row = 1
    while row<= 5:
        print_line("*",4)
        row += 1
name = "计海康"
