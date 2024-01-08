# cloures two condition parent variable has scope after return then child function.
# child function also have still parent variable scope

def parent_func(person, coins):
    # coins = 3

    def child_func():
        nonlocal coins
        coins -= 1
        print(coins)
        if coins > 1:
            print("coin value greater than 1 for this " + person, coins)
        elif coins == 1:
            print("coin value greater than 1 " + person, coins)
        else:
            print("coin value check plz s" + person, coins)
    return child_func


# aniket = parent_func("aniket")
mike = parent_func("mike", 4)

# aniket()
# aniket()
# aniket()

# mike()
# mike()


mike()
mike()
mike()
