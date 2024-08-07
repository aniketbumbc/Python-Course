from convertor import convert_into_lbs, convert_into_kg, find_max_number
from ecommerce.shipping import shipping
import random

print(convert_into_lbs(23))
print(convert_into_kg(100))

print(find_max_number([3, 5, 6, 66, 100, 2333]))

shipping()

for i in range(0, 5):
    print(random.randrange(5, 10))
