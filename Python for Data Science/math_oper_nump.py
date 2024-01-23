# Maths operations
import numpy as np


array1 = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
array2 = np.arange(0, 4)


# print(array2)

# array3 = array1 + array2


# print(array3)


arrayLinespace = np.linspace(1, 10, 5)  # Range of 5 between 1 to 10

# print(arrayLinespace*2)


# vshape, hshape and reshape


# vshapeArr = np.vstack((array1, array2))
# hshapeArr = np.hstack((array1, array2))
reshapeArr = np.reshape(array1, (1, -1))  # 3 * 3 = 9

# print(reshapeArr)


practiceArr = np.arange(132).reshape(11, 12)

# print(practiceArr)
# print(np.unravel_index(99, (11, 12)))


# print(array1)

# print(np.power(array1, 2))


# trigo


# print(np.pi)

theta = np.linspace(0, np.pi, 5)
# print(theta)
# print(np.sign(theta))


x = [1, 2, 3, 4, 5]

xNum = np.array(x)  # e = 2.718

# print(np.exp(x))

# print(np.exp2(xNum))

# print(np.power(xNum, 3))
# print(np.log(x))
# print(np.log10(x))


y = np.arange(6)

print(y)

print(np.multiply(y, 3))


# aggregates


xy = np.arange(1, 6)

print(xy)
print(np.add.reduce(xy))
print(np.add.reduce(xy))
print(np.add.accumulate(xy))


# linear alg
