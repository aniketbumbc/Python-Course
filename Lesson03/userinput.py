import sys
import random
print(" ")
playerInput = input(
    "Please enter your choice.....\n 1.Rock\n 2.Paper \n 3.Scissors \n")


playerChoiceIntegerInput = int(playerInput)

if playerChoiceIntegerInput < 1 or playerChoiceIntegerInput > 3:
    sys.exit("Please enter correct user input")


computerChoice = random.choice('123')
castIntComputerChoice = int(computerChoice)


print(" ")

print("Player choice " + " " + playerInput + " ")
print("Computer choice " + " " + computerChoice + " ")
print(" ")


if playerChoiceIntegerInput == 1 and castIntComputerChoice == 3:
    print("Player win")
elif playerChoiceIntegerInput == 2 and castIntComputerChoice == 1:
    print("Player win")
elif playerChoiceIntegerInput == 3 and castIntComputerChoice == 2:
    print("Player win")
elif playerChoiceIntegerInput == castIntComputerChoice:
    print("Tie Game!!!!!")
else:
    print("Computer win")

print(" ")
