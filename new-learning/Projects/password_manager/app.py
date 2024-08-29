master_pwd = input("what is your master password ? ")


def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, password = data.split("|")
            print("User:", user, ", Password:", password)


def add():
    name = input("Account Name: ")
    password = input("Password: ")
    # open file and automatically close
    with open('password.txt', 'a') as f:
        f.write(name + "|" + password + "\n")


while True:
    mode = input("What you would like view or add password or q to break ? ")
    if mode == "q":
        break
    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print("You are entering wrong mode")
