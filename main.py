import sys
import os
from parseCommands import parseCommands
from termcolor import colored

ACCEPTED_SHELLS = ["powershell", "cmd"]


def exitMessage():
    print(colored("Thanks For Using Miniature Shell!", "green"))


def shortenCWD(cwd: str):

    pathSepartor = '/' if os.name == 'posix' else '\\'

    idx = -1

    for i in range(len(cwd)):
        if cwd[i] == pathSepartor:
            idx = i

    idx += 1

    return cwd[idx:]


def main():
    DEBUG: bool = False
    print(colored("Welcome To Miniature Shell (mash)!", "green"))
    print(colored("Type 'help' or '?' for a list of commands", "green"))

    while True:

        try:
            line = input(
                f"{colored('mash', 'blue')} {colored(shortenCWD(os.getcwd()), 'yellow')} > ")
        except KeyboardInterrupt:
            print()
            exitMessage()
            sys.exit()

        if line == 'exit':
            exitMessage()
            sys.exit()
        elif line == 'debug':
            if DEBUG:
                DEBUG = False
            else:
                DEBUG = True
            print(f'{DEBUG=}')
            continue

        parseCommands(line, debug=DEBUG)


if __name__ == '__main__':
    main()
