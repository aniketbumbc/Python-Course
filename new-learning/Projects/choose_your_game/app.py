name = input("Type your name !!  ")
print("Welcome", name, "to your adventure")
answer = input("Choose the path left or right  ")
if answer == "left":
    print("Your path is here ", answer)
    answer = input("Now you can choose swim or walk ?")
    if answer == "swim":
        print("You need life jacket to swim in deep water")
    elif answer == "walk":
        print("You can freely walk without probelm")
    else:
        print("You are in left loop")
elif answer == "right":
    print("Your path is here ", answer)
    answer = input("Now you can choose ride on camel or horse? ")
    if answer == "camel":
        print("You seat back relax enjoy your view top ")
    elif answer == "horse":
        print("go fast rides")
    else:
        print("You are in right loop")
else:
    print("Your enter choice is incorrect")
