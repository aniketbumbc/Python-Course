class Person:

    bike = "KZM"  # class variable

    # constructor self parameter refers to current instance of the class
    def __init__(self, name, age):
        self.name = name  # instance variable
        self.age = age

    def greet(self):
        # This is a method of the Person class that prints a greeting message
        print("Hello, my name is " + self.name)
        print("Hello, my age is " + self.age)
        print(Person.bike)


p1 = Person("Aniket", "33")
p1.greet()


# inheritance


class Animal:
    def speak(self):
        print("Animal is speaking")


class Dog(Animal):
    def bark(self):
        print("Dog barking")


class DogChild(Dog):
    def noBark(self):
        print("This Dog Not barking")


d1 = Dog()
mute = DogChild()

d1.speak()
d1.bark()

mute.speak()
mute.noBark()
mute.bark()


# mulipe inheritance multiple base class with child


class Addition:
    def add(self, a, b):
        addition = a + b
        print("Addtion is ", addition)


class Multipication:
    def multi(self, a, b):
        multipy = a * b
        print("Multipication is ", multipy)


class Minus:
    def minus(self, a, b):
        minusCal = a - b
        print("Addtion is ", minusCal)


class MathCal(Addition, Multipication, Minus):
    pass


result = MathCal()

result.add(10, 20)
result.multi(20, 10)
result.minus(50, 10)
