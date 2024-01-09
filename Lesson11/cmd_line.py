
from utils_functions import hello, test
import argparse
print(__name__)


parser = argparse.ArgumentParser(
    description="Provides a personal gretting"
)

parser.add_argument("-n", "--name", metavar="name",
                    required=True, help="The name of person to greet.")

parser.add_argument("-l", "--lang", metavar="language",
                    required=True, choices=["English", "Spanish", "German"], help="Please enter language of greetings")

args = parser.parse_args()
msg = f"Hello {args.name}!"
hello(args.name, args.lang)
test()
