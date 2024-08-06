def greet_user():
    print("Hello welcome to function")
    print("practice functions")


# print("Start")
# greet_user()


def param_function(student_name):
    print(f'Hello {student_name} how are you ')


# param_function("bunny")


# positional argument and key word argument
# numerical value then use keyword argument
# use keyword argument after positional value
# by default python return None. if not return anything function

def square(num):
    return num * num


# print(square(20))


def emojiConvertor(message):
    words = message.split(' ')
    emoji = {
        ':)': "😀",
        '(:': "😫"
    }
    output = ""
    for word in words:
        if(word in emoji):
            output = emoji.get(word)

    return output


print(
    emojiConvertor("hello aniket :)"))

print(
    emojiConvertor("hello aniket (:"))
