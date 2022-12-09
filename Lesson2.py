class Student:
    print("Hi")
    def __init__(self):
        self.height = 160
        self.age = 12
        self.sex = "man"
        self.mark = 9
        self.money = 100
        print("I am alive! ")
    def printer(self):
        print(self.height)
        print(self.age)
        print(self.sex)
        print(self.mark)
    def holiday(self):
        self.money -=5
    def work(self):
        self.money +=1
Yaroslav = Student()
Alexandra = Student()
YusufKayra = Student()
Denis = Student()
Alexandra.sex = "women"
Yaroslav.printer()
Alexandra.printer()
YusufKayra.printer()
Denis.printer()
# Student.__init__(self=Alexandra)
# print(Yaroslav.height)
# print(Alexandra.height)
# print(YusufKayra.height)
# print(Denis.height)
# print(Yaroslav.age)
# print(Alexandra.age)
# print(YusufKayra.age)
# print(Denis.age)
# print(Yaroslav.sex)
# print(Alexandra.sex)
# print(YusufKayra.sex)
# print(Denis.sex)
# print(Yaroslav.mark)
# print(Alexandra.mark)
# print(YusufKayra.mark)
# print(Denis.mark)
