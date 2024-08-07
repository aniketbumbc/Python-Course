class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print("Drawing point here")

    def move(self):
        print("Moving point here")


p1 = Point(100, 200)
# print(p1.x)
# print(p1.y)
# p1.draw()
# p1.move()
# p1.y = 44000
# print(p1.y)


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'{self.name} can talk English easily')


p1 = Person('Bunny')
p1.talk()
print(p1.name)

# ************************* #
# Inheritance in Python


class Mammal:
    def Walk(self):
        print("Yaaaa !!! Mammal can walk")


class Cat(Mammal):
    def CatTalk(self):
        print("Cat can do maaaau")


class Dog(Mammal):
    def LoyalDog(self):
        print("Dog are more loyal than cat")


c1 = Cat()
c1.Walk()
c1.CatTalk()

d1 = Dog()
d1.Walk()
d1.LoyalDog()
