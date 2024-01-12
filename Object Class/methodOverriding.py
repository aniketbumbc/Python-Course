# parent class method define in the child class with some specific implementation.
# that is called method overriding. different definatoin of a parent class method is needed in the child class


##### Method overring #####


class Bank:
    def getFdReturn(self):
        return 10


class BOA(Bank):
    def getFdReturn(self):
        return 9


class ICICI(Bank):
    def getFdReturn(self):
        return 9.5


b1 = Bank()
b2 = BOA()
b3 = ICICI()


print("Bank Rate of interest:", b1.getFdReturn())
print("BOA Rate of interest:", b2.getFdReturn())
print("ICICI Rate of interest:", b3.getFdReturn())


# Data abstraction in python

# In python, we can also perform data hiding by adding the double underscore(___) as a prefix to
# the attribute which is to be hidden. After this, the attribute will not be visible outside of
# the class through the object.


class Employee:
    _count = 100

    def __init__(self):
        Employee._count = Employee.__count+1

    def display(self):
        print("The number of employees", Employee.__count)


emp = Employee()
emp2 = Employee()

#   print(emp.__count)

try:
    print(emp.__count)
except Exception as error:
    print(error)
