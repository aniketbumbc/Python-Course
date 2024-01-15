# r = read
# a = Append
# w = Write
# x = Create


# Read - error if it dosen't exits

import os
from os.path import exists
f = open("names.txt")

# print(f.read())
# print(f.read(4))

# print(f.readline())
# print(f.readline())


for line in f:
    print(line)

f.close()

# for number in range(0, 10):
#     print(number)


try:
    n = open("names.txt")
except Exception as error:
    print(error)
finally:
    print("Closing Files")
    n.close()


# h = open("names.txt", "a")
# h.write("Neil\n")
# h.write("bunny\n")
# h.close()


# h = open("names.txt")
# print(h.read())
# h.close()


# over write

# k = open("context.txt", "w")
# k .write("I deleteded all context")
# k .close()


# k = open("context.txt")
# print(k.read())
# k .close()


# create new files


j = open("name_lists.txt", "w")
j.close()


# create specified file return error if file is present

if not os.path.exists("meenu.txt"):
    f = open("meenu.txt", "x")
    f.close()

# delete file
# Avoid error

if exists("name_lists.txt"):
    # print(exists("name_lists.txt\n"))
    os.remove("name_lists.txt\n")
else:
    print("Test")
    print("file you want delete not there")
