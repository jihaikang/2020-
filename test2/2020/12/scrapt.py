def addx(x):
    def adder(y):
        return x + y #  闭包
    return adder
c=addx(8)
print(c(10))