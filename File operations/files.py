# r = read
# a = Append
# w = Write
# x = Create


# Read - error if it dosen't exits


f = open("names.txt")

# print(f.read())
# print(f.read(4))

print(f.readline())
print(f.readline())


for line in f:
    print(line)

f.close()

# for number in range(0, 10):
#     print(number)


try:
    n = open("k.txt")
except Exception as error:
    print(error)
