import sys
import getpass
from app import Session
from utils import Color

HELP_MESSAGE = """{0}Avalibale Commands:
{1}exit          {3}Exit the app
{1}my privacy    {3}Show all other users access to my information {2}check it now{3}""".format(Color.CYAN, Color.BLUE, Color.REVERSE, Color.RESET)


def do_you_sure(yse_to_all):
    if yse_to_all:
        return True
    else:
        return raw_input("Do you sure for exit: (y/n) ") == 'y'


def login():
    """
    Get username and password from user and return session object
    """
    username = raw_input("Username: ")
    password = getpass.getpass()
    # @todo Add print user login info
    return Session(username, password)


def controller(session, command):
    pass


def shell(yse_to_all=False):
    session = login()
    while (True):
        command = raw_input("> ").lower()
        if command == '-h':
            print(HELP_MESSAGE)
        elif command == 'exit' and do_you_sure(yse_to_all):
            sys.exit()
        elif command == 'my privacy':
            # @todo needs to implement by query
            print('Your Privacy')
        else:
            controller(session, command)
