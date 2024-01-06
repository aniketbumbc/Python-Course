# Tuple information
# A tuple in Python is similar to a list. The difference between the two is that
# we cannot change the elements of  a tuple once it is assigned
# whereas we can change the elements of a list.

interger_tuple = (4, 5, 6, 9.10)
rollnumbers = [55, 34, 23, 1, 67, 88, 100]

print(interger_tuple)

string_tuple = 'ehllo', 'mike', 'hows'
print(string_tuple)

print(type(string_tuple))


for intuple in interger_tuple:
    print(intuple)

for numbers in rollnumbers:
    print(numbers)


# We generally use tuples for heterogeneous (different) data types and lists for homogeneous (similar) data types.
# Since tuples are immutable, iterating through a tuple is faster than with a list. So there is a slight performance boost.
# Tuples that contain immutable elements can be used as a key for a dictionary. With lists, this is not possible.
# If you have data that doesn't change, implementing it as tuple will guarantee that it remains write-protected.
