nums = {1, 2, 3, 4, 3, 2, 1, "aniekt", True}
nums2 = set((9, 8, 7, 6, 5, 4))

band = {
    "vocals": "Plant",
    "guitar": "Page"
}
print(nums2)

# NO dupilcate value
print(5 in nums2)

# no index and key position in set

nums.add(3003)
nums.update(band)
print(nums)

# Merge two sets create one

one = {343, 545, 112, 200}
two = {200, 300, 100, 500}

newSetMerge = one.union(two)
print(newSetMerge)

# To keep only duplicate ( intersection_update)
