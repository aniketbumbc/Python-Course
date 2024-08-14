print("Welcome to computer quiz game")
playing = input("You want to play the game? ")
correct_answers = 0
wrong_answers = 0

if(playing.lower() != "yes"):
    quit()

print("Let's play the game now Play: ")

ans1 = input("What full form of CPU ? ")
if(ans1.lower() == 'central processing unit'):
    print("correct")
    correct_answers += 1
else:
    print("Sorry Wrong Answer")
    wrong_answers += 1


ans2 = input("ICC related for ? ")
if(ans2.lower() == 'cricket'):
    print("correct")
    correct_answers += 1
else:
    print("Sorry Wrong Answer")
    wrong_answers += 1

ans3 = input("BCCI related for ? ")
print(ans3)
if(ans3.lower() == 'india cricket'):
    print("correct")
    correct_answers += 1
else:
    print("Sorry Wrong Answer")
    wrong_answers += 1

ans4 = input("FIFA ? ")
if(ans4.lower() == 'football'):
    print("correct")
    correct_answers += 1
else:
    print("Sorry Wrong Answer")
    wrong_answers += 1

if(correct_answers > 2):
    print("Yesssss You Are Winner")
else:
    print("Lost The Game")
    quit()
