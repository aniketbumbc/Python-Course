print("Welcome to lab to play quiz!!!!")

playing = input("Do you want to play ?\n")

if playing.lower() != "yes":
    quit()

print("Okay!!! Let's Play 🎉")
score = 0

answer = input("What is meaning of CPU ? \n").lower()
if answer == "central process units":
    print("Correct !!! ✅")
    score += 1
else:
    print("Incorrect !!! ❌")

answer = input("What meaning GPU \n").lower()
if answer == "game process units":
    print("Correct !!! ✅")
    score += 1
else:
    print("Incorrect !!! ❌")


answer = input("What is RAM meaning ? \n").lower()
if answer == "random access memory":
    print("Correct !!! ✅")
    score += 1
else:
    print("Incorrect !!! ❌")

print(f"You got {score} questions correct 🥳🥳🥳")
