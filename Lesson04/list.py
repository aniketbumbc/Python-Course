# list like array in other languages

users = ["Dave", "Jhon", "Sara"]
data = ['Bomb', 43, True]

# print(users)
# print(users[0:1])
# print(len(users))


# added users


users.append('Elsa')  # added users
# print(len(users))
users += ['Elsa Craig']
# print(users)
users.extend(data)
# print(users)
users.insert(0, "Aniket")
# print(users)
users[2:2] = ["Mike", "Fold"]
# print(users)
# print(users.index("Mike"))

# Removed Data from list


# print(users)
users.remove("Aniket")
users.pop()
# print("")
users.pop()
# print(users)


# sort list


# users.sort()
users[1:2] = ["Yahooo", "Yashoo", "Mike-1"]
print("")
# print(users)
# print(type(users))
print("Yashoo" in users)
users[0:1] = ["acricket", 'aafootball']
users.sort()
# print(users)
users.sort(key=str.lower)
print("")
# print(users)

# Number list

rollnumbers = [55, 34, 23, 1, 67, 88, 100]
print("og", rollnumbers)

# rollnumbers.reverse()
# print("")
# print(rollnumbers)
print("")
print(sorted(rollnumbers, reverse=True))
# print("")
# print(rollnumbers)

# list not modify original list keep same as it is
print("OG", rollnumbers)

# create copy or another list


rollnumbersCopy = rollnumbers.copy()
myRolls = list(rollnumbers)
rollnumbersCopy.sort()
print(rollnumbersCopy)
print(myRolls)

# Tuples
# Data in tuple will not change
# Order Data in tuple will not change
