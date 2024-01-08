# recurssion
def add_one(num):
    if (num >= 9):
        return num + 1

    total = num + 1
    print(total)

    return add_one(total)


# add_one(2)


# function loop practice

def loop_func(num):
    temp_num = 0
    while temp_num < num:
        temp_num += 1
        print(temp_num)


loop_func(10)


value = True
