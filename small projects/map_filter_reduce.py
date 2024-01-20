countries = ["India", "USA", "Italy", "France"]

# for country in countries:
#     print(country.upper())

upperCase = []

# for country in countries:
#     upperCase.append(country.upper())


# print(upperCase)


# Map (function, collection of list) output list


map_practice = map(lambda a: a.upper(), countries)


# for b in map_practice:
#     print(b)


L1 = [4, 5, 6, 7, 10, 12, 14, 16]

# square_l1 = map(lambda x: x**2, L1)
# for num in square_l1:
#     # print(num)


# def square_it(n):
#     print(n)
#     return n*n


# L2 = map(square_it, L1)


# for num in L2:
#     print(num)


# Filter #####

def div_by_two(x): return x % 2 == 0


# print(div_by_two(100))

div_by2 = filter(div_by_two, L1)

# print(list(div_by2))


students_data = {1: ['Sam', 15], 2: ['Rob', 18], 3: [
    'Kyle', 16], 4: ['Cornor', 19], 5: ['Trump', 20]}


def filter_data(x): return x[1] >= 18


get_filter = filter(filter_data, students_data.values())

print(list(get_filter))
