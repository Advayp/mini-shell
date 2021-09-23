from commands import COMMAND_LIST_NO_ARGS, COMMAND_LIST_ONE_ARG
from termcolor import colored


def showHelpMessage(key, value):
    print("---")
    print(f"Name: {key}\nDescription: {value.description}\n{value.usage}")
    print("---")


def parseCommands(line: str, debug=False, shellName='powershell'):
    keywords = line.split(' ')

    if line.strip() == 'help' or line.strip() == '?':
        print("------ INFO -----")
        for key, value in COMMAND_LIST_NO_ARGS.items():
            showHelpMessage(key, value)

        for key, value in COMMAND_LIST_ONE_ARG.items():
            showHelpMessage(key, value)

        return

    if debug:
        print(keywords)

    if len(keywords) == 1:
        command = keywords[0].lower()
        try:
            COMMAND_LIST_NO_ARGS[command].use()
        except KeyError:
            print(colored(f"AdvayShell: Command {command} not found", "red"))
        except:
            print(colored("Error Occured", "red"))

    elif len(keywords) == 2:
        command = keywords[0].lower()
        arg = keywords[1]
        try:
            COMMAND_LIST_ONE_ARG[command].use(arg)
        except KeyError:
            print(colored(f"AdvayShell: Command {command} not found", "red"))
