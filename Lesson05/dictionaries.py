# Dictionaries

band = {
    "vocals": "Plant",
    "guitar": "Page"
}

student = dict(name="mike", age=34)


# print(band)
# print(student)

# Access Element

# print(band["guitar"])
# print(student.get("age"))


# list all keys and values

# print(student.keys())
# print(student.values())
# print(student.items())

# verify key exit or not
# print("age" in student)

# change values

student["age"] = "kartik"
student.update({"city": "pune"})

# print(student)

# Remove value


print(student.pop("age"))
# print(student)

# delete and clear items

del student["city"]
student["age"] = "kartik"
student.update({"city": "pune"})
# print(student)

# Copy dictionary

newStudent = student.copy()  # creates different reference with newStudent
newStudent["city"] = "Mumbai"
# print(newStudent)

# dic constructor function

futureStudent = dict(newStudent)
futureStudent["city"] = "Baltimore"
# print(futureStudent)

# Nested dictionary

print("")

nestedIndo = {
    "student": student,
    "band": band
}


print(nestedIndo)

print(nestedIndo["band"]["vocals"])
