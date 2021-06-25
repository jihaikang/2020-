class Cat():
    def eat(self):
        print("小猫爱吃鱼")
    def drink(self):
        print("小猫爱喝水")
tom = Cat()

tom.eat()
tom.drink()
print(tom)
# 在创建一个猫对象
lazee_cat = Cat()
lazee_cat.eat()
lazee_cat.drink()
print(lazee_cat)
laze2_Cat = lazee_cat
print(lazee_cat)