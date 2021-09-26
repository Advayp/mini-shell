from commandDefinitions import *


class Command:
    def __init__(self, name, action, usage, description=None) -> None:
        self.name = name
        self.action = action
        self.description = description
        self.usage = usage

    def use(self, *args):
        self.action(*args)


COMMAND_LIST_NO_ARGS: dict[str, Command] = {
    "printdir": Command("printdir", printDir, "Usage: printdir", description='List Contents of the Current Directory'),
    "pd": Command("printdir", printDir, "Usage: pd", description='List Contents of the Current Directory'),
    "cd..": Command("Change Directory", changeDirOneBack, "Usage: cd..", description='Go Back One Directory'),
    "ping": Command("Ping", ping, "Usage: ping", description="A command made for fun!")
}

COMMAND_LIST_ONE_ARG: dict[str, Command] = {
    "printdir": Command("printdir", printExternalDir, "Usage: printdir $PATH_TO_DIR", description='List Contents Of A Directory'),
    "pd": Command("printdir", printExternalDir, "Usage: printdir $PATH_TO_DIR", description='List Contents Of A Directory'),
    "cd": Command("Change Directory", changeDir, "Usage: cd $PATH_TO_DIR", description='Change CWD'),
    "open": Command("Open", open, "Usage: open $FILE_NAME", description="Opens A File"),
    "create": Command("Create", create, "Usage: create $FILE_NAME", description="Creates A File"),
    "read": Command("Read", read, "Usage: read $FILE_NAME", description="Reads A File"),
    "echo": Command("Echo", echo, "Usage: echo $TEXT", description="Prints Text To The Console"),
    "printenv": Command("PrintEnv", readEnv, "Usage: printenv $ENV_NAME", description='Prints an Environment Variable')
}

COMMAND_LIST_TWO_ARGS: dict[str, Command] = {
    "setenv": Command("Set Env", addEnv, "Usage: setenv $ENV_NAME $VALUE", description="Sets and Environment Variable")
}
