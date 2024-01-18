l = [1, 1, 2, 3, 3, 5, 5, 6, 6]


set_l = set(l)
print(set_l)
print(type(set_l))
print(len(set_l))

new_set = {1, 3, 5, 6, 7, 1}

print(new_set)
new_set.add("Aniket")
new_set.add("bunny")
print(new_set)

new_set.remove("Aniket")
print(new_set)


A = {0, 2, 4, 6, 8}

B = {1, 2, 3, 4, 5}


# print(A | B)  # union operator
# print(A.union(B))


# print(A & B)  # intersection both common
# print(A.intersection(B))

# print(A - B)  # difference unique value in A which are not B

# sematric difference is value no intersection value and
# values that are unique in A and B
# either in A and either B


# print(A ^ B)


# print("Test", (A.union(B)).difference(A.intersection(B)))

# {0, 1, 2, 3, 4, 5, 6, 8}.difference {2, 4}
# {0,1,3,5,6,8}

C = [5, 5, 5, 5, 5, 5, 5, 3]
D = [3, 3, 5, 5, 1, 7, 2]

set_list_1 = set(C)
set_list_2 = set(D)

# unique_list = (set_list_1 ^ set_list_2)
answer_demo = set_list_1 & set_list_2

temp_list = list(answer_demo)

print((temp_list))
test = sorted(temp_list)
print(test)
