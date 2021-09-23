import sys
import os
from parseCommands import parseCommands
from termcolor import colored
from time import sleep, time

ACCEPTED_SHELLS = ["powershell", "cmd"]


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
    print(colored("Welcome To AdvayShell!", "green"))
    print(colored("Type 'help' or '?' for a list of commands", "green"))
    sleep(0.5)

    while True:

        try:
            line = input(
                f"{colored('AS', 'blue')} {colored(shortenCWD(os.getcwd()), 'yellow')} > ")
        except KeyboardInterrupt:
            print()
            print(colored("Thanks For Using AdvayShell!", "green"))
            sys.exit()

        if line == 'exit':
            print(colored("Thanks For Using AdvayShell!", "green"))
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
