import numpy as np
from numpy.core.fromnumeric import size


arr = np.ones(5, dtype=int)
# print(arr.dtype)

# print(arr)


# multi dim array

multiArr = np.ones((3, 3))

# print(multiArr)

zeros = np.zeros(5, dtype=int)

# print(zeros)


rangeArr = np.arange(4.0)

# print(rangeArr)

stepArr = np.arange(3, 100, 2)

# print(stepArr)


# print(np.random.randint(4, 10, size=10))  # lower include and upper exclude


# Create an array of first 10 multiples of 5 using the 'arange' function.

mulFive = np.arange(5, 55, 5)

# print(mulFive)


# 2D random integer
twoDNumArr = np.random.random([2, 2])  # Rows([row,coloumn])
print(twoDNumArr)


linerSpace = np.linspace(1, 10, 20)
# print(linerSpace)


print(np.random.randint(0, 3, size=4))
