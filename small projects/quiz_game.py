print("Welcome to lab to play quiz!!!!")

playing = input("Do you want to play ?\n")

if playing.lower() != "yes":
    quit()

print("Okay!!! Let's Play 🎉")

answer = input("What is meaning of CPU ? \n")
if answer == "central process units":
    print("Correct !!! ✅")
else:
    print("Incorrect !!! ❌")

answer = input("What meaning GPU \n")
if answer == "game process units":
    print("Correct !!! ✅")
else:
    print("Incorrect !!! ❌")


answer = input("What is RAM meaning ? \n")
if answer == "random access memory":
    print("Correct !!! ✅")
else:
    print("Incorrect !!! ❌")
