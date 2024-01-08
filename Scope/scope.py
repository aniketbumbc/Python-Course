name = "Dave"  # Global scope
count = 100


def gretting():
    color = "blue"
    print(name)


gretting()


# Clourse


def first_function():
    call_func1 = 10
    print("Hello First Function")

    def second_func():
        call_func2 = 20
        global count
        count += 200
        nonlocal call_func1
        call_func1 = 1000
        print("Second func call", call_func1)
        print(name, count)
        print("Second func call", call_func2)

    second_func()


first_function()
