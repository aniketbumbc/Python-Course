# loops and more progressive practice
# loops

# for item in ['Python', 'Java', 'Java Script']:
#     print(item)

# Print number 1 to 10 range function with object

# for numberItem in range(30, 41, 3):
#     print(numberItem)

# Nested loop one loop inside another

# for x in range(4):
#     for y in range(3):
#         print(f'({x},{y})')

# print F on screen

# numbers = [5, 2, 5, 2, 2]
# for value in numbers:
#     print(value * 'X')

# langues = ['Python', 'Java', 'Java Script', 'HTML', 'CSS', 'Native']
# print(langues)
# print(langues[3:5])

# Find large number from list
# numbers = [3, 4, 6, 100, 7, 19, 39, 59]
# largeNumber = numbers[0]
# for item in numbers:
#     if(item > largeNumber):
#         largeNumber = item
# print("Then large number is ", largeNumber)

# # 2D list
# matrix = [[1, 2, 3], [100, 200, 300], [1000, 2000, 3000]]
# for row in matrix:
#     for item in row:
#         print(item)

# langues = ['Python', 'Java', 'Java Script', 'HTML', 'CSS', 'Native']
# langues.append("C++")
# print('old items', langues)
# langues.insert(2, "C")
# langues.remove("HTML")
# print("HTML" in langues)  # Check number
# langues.sort()
# print(langues)
# langues.reverse()
# print(langues)
# copy_list = langues.copy()
# print(copy_list)

# Remove duplicate item list
# duplicate_item_list = [1, 2, 4, 4, 2, 1, 5, 5, 10]
# unique_list = []

# for item in duplicate_item_list:
#     if not (item in unique_list):
#         unique_list.append(item)
# print(unique_list)

# tuples
# simpler to list can not change it or add or delete from it

# count method returns the number of times a specified value appears in the tuple.

# numbers = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
# print(numbers.count(7))
# print(numbers.index(8))

# unpacking

# coordinates = (1, 3, 7, 8)
# a, s, d, f = coordinates
# print(a, s, d, f)

# disctorinies like key, value pair

customer = {
    "name": "Mike",
    "age": 23,
    "city": "Baltimore",
    "is_verify": True
}

print(customer)
print(type(customer))
print(customer['age'])
print(customer.get('is_verifyw'))
customer["school"] = "UMBC"
print(customer)
