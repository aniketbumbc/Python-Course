# Maths operations
import numpy as np


array1 = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
array2 = np.arange(0, 4)


print(array2)

# array3 = array1 + array2


# print(array3)


arrayLinespace = np.linspace(1, 10, 5)  # Range of 5 between 1 to 10

print(arrayLinespace*2)


# vshape, hshape and reshape


# vshapeArr = np.vstack((array1, array2))
# hshapeArr = np.hstack((array1, array2))
reshapeArr = np.reshape(array1, (1, -1))  # 3 * 3 = 9

# print(reshapeArr)


practiceArr = np.arange(132).reshape(11, 12)

print(practiceArr)
print(np.unravel_index(99, (11, 12)))
