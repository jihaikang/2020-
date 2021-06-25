# def test1():
#     print("*" * 50)
#     print("test 1")
#     print("*" * 50)
#
#
# def test2():
#     print("-" * 50)
#     print("test 2")
#
#     test1()
#
#     print("-" * 50)
#
#
# test2()
def print_line(char, times):
    print(char * times)


def print_lines(char, times):
    row = 0

    while row < 5:
        print_line(char, times)

        row += 1
name = "计海康"


