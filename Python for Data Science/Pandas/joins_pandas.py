
import pandas as pd


skills = pd.read_csv('LOR.csv', header=0)
age = pd.read_csv('LOTR 2.csv', header=0)

print(skills)
print(age)


# Merge two Data frames  Inner Join
#  Only common items between two data frames as output
# Match common id/key
#  #####

inner_merge = skills.merge(age, how="inner", on=['FellowshipID', 'FirstName'])

# print(inner_merge)


# Merge two Data frames  Outer Join Full
#  combine two data frames as output into one
# overlapping won't duplicate
#  #####

outer_merge = skills.merge(age, how='outer')

# print(outer_merge)


# Merge two Data frames  Full data from left data frame Left Join Full
#  combine two data frames as output into one
# overlapping from left get into right duplicate
#  #####

left_merge = skills.merge(age, how="left")

print(left_merge)

# Merge two Data frames  Full data from right data frame right Join Full
#  combine two data frames as output into one
# overlapping from right get into left duplicate
#  #####


right_merge = skills.merge(age, how="right")

print(right_merge)


# Cross data frame ( Cross Join )
#  combine two data frames as output into one
# overlapping from right get into left duplicate
#  #####


cross_merge = skills.merge(age, how="cross")

# print(cross_merge)


# ********* Concatinating *******************

concat_df = pd.concat([skills, age])

print(concat_df)

# concat with inner join
concat_df_inner = pd.concat([skills, age], join='inner')

print(concat_df_inner)
