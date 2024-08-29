from cryptography.fernet import Fernet


'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key) '''


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


master_pwd = input("what is your master password ? ")
key = load_key()
fer = Fernet(key)


def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, password = data.split("|")
            print("User:", user, "| Password:",
                  fer.decrypt(password.encode()).decode())


def add():
    name = input("Account Name: ")
    password = input("Password: ")
    # open file and automatically close
    with open('password.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(password.encode()).decode() + "\n")


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
