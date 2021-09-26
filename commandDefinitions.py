import os

WINDOWS_SEPERATOR = "\\"

_ENV = {}


def printDir(*args):
    os.system('dir')


def printExternalDir(*args):
    os.system(f'dir {args[0]}')


def changeDir(*args: list[str]):
    os.chdir(args[0])


def changeDirOneBack(*args):
    os.chdir('..')


def open(*args):
    os.system(f'.\\{args[0]}')


def create(*args):
    os.system(f'echo "" > {args[0]}')


def read(*args):
    os.system(f'type {args[0]}')


def ping(*args):
    print("Pong!")


def echo(*args):
    print(args[0])


def addEnv(*args):
    _ENV[args[0]] = args[1]


def readEnv(*args):
    if args[0] in _ENV.keys():
        print(_ENV[args[0]])
        return
    print()
