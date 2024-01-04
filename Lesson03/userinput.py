import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


print(" ")
playerInput = input(
    "Please enter your choice.....\n 1.Rock\n 2.Paper \n 3.Scissors \n")


playerChoiceIntegerInput = int(playerInput)

if playerChoiceIntegerInput < RPS.ROCK.value or playerChoiceIntegerInput > RPS.SCISSORS.value:
    sys.exit("Please enter correct user input")


computerChoice = random.choice('123')
castIntComputerChoice = int(computerChoice)


print(" ")

print("Player choice " + " " + str(RPS(playerChoiceIntegerInput)) + " ")
print("Computer choice " + " " + str(RPS(castIntComputerChoice)) + " ")
print(" ")


if playerChoiceIntegerInput == RPS.ROCK.value and castIntComputerChoice == RPS.SCISSORS.value:
    print(" 🎉Player win")
elif playerChoiceIntegerInput == RPS.PAPER.value and castIntComputerChoice == RPS.ROCK.value:
    print("🎉 Player win")
elif playerChoiceIntegerInput == RPS.SCISSORS.value and castIntComputerChoice == RPS.PAPER.value:
    print("🎉 Player win")
elif playerChoiceIntegerInput == castIntComputerChoice:
    print(" 🥺 Tie Game!!!!!")
else:
    print("🤟🏻 Computer win")

print(" ")
