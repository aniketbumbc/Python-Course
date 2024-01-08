person = "Dave"
coins_pocket = 3


message = "%s has %s conins left" % (person, coins_pocket)
print(message)


player = {"score": 12, "country": "India"}

testMessage = "\n{person} win the game by {coins_pocket} coins".format(
    person="bunny", coins_pocket=2)
print(testMessage)


# Fstring

message = f"\n{person.lower()} has {coins_pocket} coins for the game"
print(message)


for num in range(0, 10):
    print(f"\n{person.lower()} has {num * 2} coins for the game")
