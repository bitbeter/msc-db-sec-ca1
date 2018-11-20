import sys
import getpass
from app import Session
from app.utils import Color
from prompt_toolkit import prompt
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.shortcuts import yes_no_dialog

HELP_MESSAGE = """{0}Avalibale Commands:
{1}exit          {3}Exit the app
{1}<query>       {3}Select, Insert and update
{1}my privacy    {3}Show all other users access to my information {2}check it now{3}""".format(Color.CYAN, Color.BLUE, Color.REVERSE, Color.RESET)

SHELL_COMPLETER = WordCompleter(
    ['exit', 'my privacy', 'select', 'insert into', 'where',  'update', 'from', 'set', 'values'])


def do_you_sure(yse_to_all):
    if yse_to_all:
        return True
    else:
        return yes_no_dialog(
            title='Yes/No',
            text='Do you sure?')


def login():
    """
    Get username and password from user and return session object
    """
    username = prompt('Username: ')
    password = prompt('Password: ', is_password=True)
    # @todo Add print user login info
    return Session(username, password)


def query(session, command):
    pass


def shell(yes_to_all=False):
    promptSession = PromptSession()
    session = login()
    while (True):
        command = promptSession.prompt(
            '> ', completer=SHELL_COMPLETER, auto_suggest=AutoSuggestFromHistory()).lower()
        if command == '-h':
            print(HELP_MESSAGE)
        elif command == 'exit' and do_you_sure(yes_to_all):
            sys.exit()
        elif command == 'my privacy':
            # @todo needs to implement by query
            print('Your Privacy')
        else:
            query(session, command)
