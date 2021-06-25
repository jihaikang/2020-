class Cat():
    def eat(self):
        print("%s爱吃鱼"%self.name)
    def drink(self):
        print("%s爱喝水"% self.name)

tom = Cat()
# 可以利用.属性名，利用赋值语句就可以了，在类的外部给类添加属性
tom.name = "tom"

tom.eat()
tom.drink()
print(tom)
# 在创建一个猫对象
lazee_cat = Cat()
lazee_cat.name = "大懒猫"
lazee_cat.eat()
lazee_cat.drink()
print(lazee_cat)
laze2_Cat = lazee_cat
print(lazee_cat)