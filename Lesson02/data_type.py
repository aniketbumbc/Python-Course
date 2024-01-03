# Data types

# 1. Strings


import math
first = "Bob"
last = "The Builder"

# print(type(last))
# print(type(last) == str)
# print(isinstance(last, str))

# construction function

# pizza = str('veggie')
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))


# string concatination

fullname = first + ' ' + last

fullname += " Hello "
# print(fullname)

# casting the number to string
decade = str(2040)
statement = "Mike will going to moon in " + decade
# print(statement)

# multiple lines

multiline = '''
this is how multiline 
            works $
                    just checking

 '''

# print(multiline)

# String methods
# print(last.lower())
# print(last.upper())
# print(multiline.title())
# print(last.replace('Builder', 'Jhon'))
# print(len(last))

# strip is used for removed white space in the sentences
# stripl removed white space from leftside
# stripr removed right space from right side

# Build Menu

title = "menu".upper()
print(title.center(20, "*"))
print("Coffe".ljust(16, '.') + "$5".rjust(4))
print("Muffine".ljust(16, '.') + "$15".rjust(4))
print("Chesse Cake".ljust(16, '.') + "$10".rjust(4))

# String Index Value

print(last)
print('')
print(last[len(last) - 1])
print('')
print(last[0:3])  # Range of string
print('')
print(last[0:])  # getting all strings

# Boolean return string value

# print(last.startswith('T'))
# print(last.endswith('r'))

# Numeric Data Type
# integer
price = 100
best_price = int(20)

# print(type(price))
# print(type(best_price))
# print(isinstance(price, int))

# Float
gpa = 3.353
# print(type(gpa))
# print(isinstance(gpa, float))

# Built in function in number

# print(abs(gpa))
# print(round(gpa))
# print(round(gpa, 1))

# print(round(math.pi, 1))

# string casting to number
zip_code = "421301"
print(type(zip_code))
zip_value = int(zip_code)
print(type(zip_value))
