

def hello(name, lang):
    grettings = {
        "English": "Hello",
        "Spanish": "Hola",
        "German": "Halllllo"
    }
    msg = f"{grettings[lang]}  {name}!!!!!!"
    print(msg)


def test():
    print("Testing Hello")
