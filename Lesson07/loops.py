num = 1

# While Loop

# while num <= 10:
#     print(num)
#     if num == 6:
#         break
#     num += 1


# For loop
users = ["Dave", "Jhon", "Sara"]
habits = ["Eats", "Sleeps", "Work"]

# for name in users:
#     print(name)

# for x in range(0, 102, 2):
#     print(x)
# else:
#     print("It's over")


for user in users:
    for habit in habits:
        print(user + " " + habit + ".")
