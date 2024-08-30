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
players_scores = [0 for _ in range(players_input)]


print(players_scores)
