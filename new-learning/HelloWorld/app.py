# print("Hello Python world")
# print('o----------')
# print('||||')
# print('*' * 20)

# price = 10
# price = 120
# rating = 4.9
# name = "Marsh"
# is_published = True

name = "Mike"
age = 20
is_new_patient = True

# print(name)
# print(age)
# print(is_new_patient)

#  Getting input from user

# name = input('What is your name? ')
# print("hello " + name)

# Type conversion
# getting typeof variable

# birth_year = input("Birthday year ")
# print(type(birth_year))
# age = 2020 - int(birth_year)  # convert into string
# print(age)

# python string dynamic string

msg = 'hello how are you'
# print(msg[2])
# print(msg[0:3])
# print(msg[:])
end_msg = " I am good"

# print(f'{msg}? Yes{end_msg}')

# python string
# course = "Python for beginners"
# print(len(course))
# print(course.upper())
# print(course.lower())
# print(course.find('be'))  # to get index of letter
# print(course.replace('for', 'to'))
# print(course)
# resultText = 'Python' in course  # return boolean value true or False
# print(resultText)

# python arithmathic paranthisis, exponentiation, multi or division and addition, subtraction
x = 10+3 * 9
# print(x)
y = 20.6
# print(round(y))

# if statement

# is_hot = ""
# is_cold = ""

# if is_hot:
#     print("It's hot day")
#     print("It's enjoy your day")
# elif is_cold:
#     print('Wear raincoat')
# else:
#     print('Sleep with AC ON')

# logical operator ie AND, OR , NOT

# convert pound weight or kg weight
# weight = int(input("Please Enter you weight: "))
# pound_or_kg = input("please enter l for pound and k: ")

# if pound_or_kg == 'k' or pound_or_kg == 'K':
#     print(f"{weight / 2} Lbs")
# elif pound_or_kg == 'l' or pound_or_kg == 'L':
#     print(f"{weight*2} Kg")
# else:
#     print("You enter wrong char")

# while loop
# i = 1
# while i <= 5:
#     print("*" * i)
#     i += 1
# print("Done")

# Game while loop

exitNumber = 9
counter = 1
while counter <= 3:
    guessNumber = int(input("Guess: "))
    if(guessNumber != exitNumber):
        counter += 1
    if(guessNumber == exitNumber):
        print("You won")
        break
else:
    print("You Fail")

# guessNumber = (input("Guess: "))

# print(type(guessNumber))
