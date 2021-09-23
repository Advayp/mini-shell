import os

WINDOWS_SEPERATOR = "\\"


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


def printEnv(*args):
    os.system("set")


def ping(*args):
    print("Pong!")


def echo(*args):
    print(args[0])
