from commands import COMMAND_LIST_NO_ARGS, COMMAND_LIST_ONE_ARG, COMMAND_LIST_TWO_ARGS
from termcolor import colored


def showHelpMessage(key, value):
    print("---")
    print(f"Name: {key}\nDescription: {value.description}\n{value.usage}")
    print("---")


def commandErrorMessage(command):
    print(colored(f"mash: Command \"{command}\" not found", "red"))


def parseCommands(line: str, debug=False, shellName='powershell'):
    keywords = line.split(' ')

    command = keywords[0].lower()

    if line.strip() == 'help' or line.strip() == '?':
        print("------ INFO -----")
        for key, value in COMMAND_LIST_NO_ARGS.items():
            showHelpMessage(key, value)

        for key, value in COMMAND_LIST_ONE_ARG.items():
            showHelpMessage(key, value)

        return

    if line.strip() == '':
        return

    if debug:
        print(keywords)

    if len(keywords) == 1:
        try:
            COMMAND_LIST_NO_ARGS[command].use()
        except KeyError:
            commandErrorMessage(command)
        except:
            print(colored("Error Occured", "red"))

    elif len(keywords) == 2:
        arg = keywords[1]
        try:
            COMMAND_LIST_ONE_ARG[command].use(arg)
        except KeyError:
            commandErrorMessage(command)

    elif len(keywords) == 3:
        args = keywords[1:]
        try:
            COMMAND_LIST_TWO_ARGS[command].use(*args)
        except KeyError:
            commandErrorMessage(command)
    else:
        commandErrorMessage(command)
