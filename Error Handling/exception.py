

try:
    print(x)
except Exception as error:
    print(error)


y = 2
try:
    print(y / 0)
except Exception as error:
    print(error)
else:
    print("No Error")
finally:
    print("I am going to print with or without error")
