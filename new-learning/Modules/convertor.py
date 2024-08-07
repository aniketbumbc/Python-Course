def convert_into_lbs(weight):
    return weight * 0.45


def convert_into_kg(weight):
    return weight / 0.45


def find_max_number(list_number):
    max_number = 0
    for num in list_number:
        if(num > max_number):
            max_number = num

    return max_number
