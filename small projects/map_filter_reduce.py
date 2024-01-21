from functools import reduce
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

# print(list(get_filter))


## Reduce # ************* ########

reduce_list = range(1, 5)


def f(x, y): return x*y


q = reduce(f, reduce_list)

# print(q)


input_list = ['Santa Cruz', 'Santa fe', 'Mumbai', 'Delhi']


def count_s(str):
    counter = 0
    if (str.startswith('S')):
        counter += 1
    return counter


count = map(count_s, input_list)

print(sum(count))

multi_arr = [['Ankur', 'Avik', 'Kiran', 'Nitin'],
             ['Narang', 'Sarkar', 'R', 'Sareen']]


first_name_new = multi_arr[0]
last_name_new = multi_arr[1]


# def test_ele(x, y): return x + " " + y


name = list(map(lambda x, y: x + " " + y, first_name_new, last_name_new))

# print(name)


student = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
           26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]


result_studnet = list(filter((lambda x: x % 5 == 0), student))

# print(result_studnet)


shopes = ['soap', 'sharp', 'shy', 'silent', 'ship', 'summer', 'sheep']


shopes_filter = list(
    filter((lambda x: x.startswith('s') and x.endswith('p')), shopes))


print(shopes_filter)


# reduce

input_list = ['I', 'Love', 'Python']

get_list_result = reduce(lambda x, y: x + ' ' + y, input_list)

print(get_list_result)

find_max = [31, 63, 76, 89]

find_max_result = reduce(lambda x, y: max(x, y), find_max)

print(find_max_result)
