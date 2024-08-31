import random


def roll():
    min_value = 1
    max_value = 6
    roll_value = random.randint(min_value, max_value)

    return roll_value


while True:
    players_input = input("Enter the number of players... 2:4 ")
    if players_input.isdigit():
        players_input = int(players_input)
        if 1 <= players_input <= 4:
            break
        else:
            print("Players between 2-4")

    else:
        print("Invalid entry, Please try again later")

max_score = 50
current_score = 0
players_scores = [0 for _ in range(players_input)]

while max(players_scores) < max_score:
    should_roll = input("Would you like to roll (y)? ")
    if should_roll == "y":
        value = roll()
    else:
        break

    if value == 1:
        print("You rolled a 1 ! Turn Done !")
        print("Your current score is ", current_score)
        break
    else:
        current_score += value

    print("Your current score is ", current_score)
