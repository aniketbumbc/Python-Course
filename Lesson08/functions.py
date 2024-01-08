# Functions

def hello_word():
    print("Welcome to hello function")


hello_word()


def sum(num1, num2=1000):
    print(type(num1))
    return num1 + num2


# total = sum(100)
# print("The addition of two number is ", total)
# sum(1300, 200)
# sum(500, 100)


# default value to parameter

def multiple_items(*args):
    print(len(args))
    parma1, param2 = args
    print(parma1, param2)
    print(type(args))


multiple_items("Hello", "World")
