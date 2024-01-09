# lambda function is the single experssion that return the value
# anonymous function which return value. No need to call function
# assign lamda to variable. that variable store that function


from functools import reduce
def squared(num): return num * num
# lambda num : num * num


print(squared(10))


def addTwo(num): return num + 2


print(addTwo(34))


def multipy(a, b): return a * b


# lamda a,b: a * b
print(multipy(10, 8))

##################################


def funBuilder(x):
    return lambda num: num * x


mulTen = funBuilder(10)
mulHundered = funBuilder(100)

print(mulTen(2))
#

################################## Higher order function ###################

# function that takes one or more function as arguments
# function return function as result


lambda num: num * num

numbers = [2, 5, 7, 3, 1, 0, 4, 6, 10, 100, 111]

squred_nums = map(
    lambda num: num * num, numbers)


print(list(squred_nums))

################################## Filter ###############

lambda num: num % 2 != 0

odd_nums = filter(lambda num: num % 2 != 0, numbers)


print(list(odd_nums))


################################## Filter ###############


addtion_numbers = reduce(lambda acc, curr: acc + curr, numbers, 200)

print(addtion_numbers)
print(sum(numbers))
