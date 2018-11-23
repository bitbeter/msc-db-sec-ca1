import sys
import getpass
from app.session import Session
from app.utils import Color
from prompt_toolkit import prompt
from prompt_toolkit import PromptSession
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.shortcuts import yes_no_dialog
from pygments.lexers.sql import SqlLexer
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.lexers import PygmentsLexer
from terminaltables import AsciiTable

HELP_MESSAGE = """{0}Avalibale Commands:
{1}exit          {3}Exit the app
{1}<query>       {3}Select, Insert and Update
{1}my privacy    {3}Show all other users access to my information {2}check it now{3}""".format(Color.CYAN, Color.BLUE, Color.REVERSE, Color.RESET)


SHELL_COMPLETER = WordCompleter(
    words=[
        # Commands
        'exit', 'MY PRIVACY', 'CREATE-USER', 'UPDATE-ACCESS', 'REMOVE-USER',
        # Query Keywords
        'SELECT', 'INSERT INTO',
        'WHERE',  'UPDATE', 'FROM', 'SET', 'VALUES',
        'AND', 'OR', 'NOT',
        # Tables name
        'doctor', 'nurse', 'employee', 'patient',
        # Columns
        'username', 'password', "firstname", "lastname", "national_code", "sexual", "birthday", 
        "maried", "section", "employee_id", "employment_date", "salary", "major", "carrer",
        "doctor_username", "nurse_username"
    ],
    ignore_case=True)


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
    return Session(username, password)


def shell(yes_to_all=False):
    promptSession = PromptSession(
        lexer=PygmentsLexer(SqlLexer), auto_suggest=AutoSuggestFromHistory()
    )
    appSession = Session('admin', 'admin')
    # appSession = None
    # while (True):
    #     try:
    #         appSession = login()
    #         break
    #     except ValueError as error:
    #         print(error)
    while (True):
        command = promptSession.prompt(
            '> ', completer=SHELL_COMPLETER
        ).lower()
        if command == '-h':
            print(HELP_MESSAGE)
        elif command == 'exit':
            if do_you_sure(yes_to_all):
                appSession.close_connections()
                sys.exit()
        elif command == 'my privacy':
            # @todo needs to implement by query
            print('Your Privacy')
        elif command == 'create-user':
            user_culomns = []
            username = None
            id = None
            type_of_user = None
            for input in ["username", "password", "type", "absolute_security_level", "read_security_level", "write_security_level", "absolute_integrity_level", "read_integrity_level", "write_integrity_level"]:
                answer = promptSession.prompt(input + ': ')
                user_culomns.append(answer)
                if input == "type":
                    type_of_user = answer
                if input == "username":
                    username = answer
            appSession.create_user(user_culomns)
            if type_of_user == "doctor":
                culomns = []
                for input in ["firstname", "lastname", "national_code", "sexual", "birthday", "maried", "section", "employee_id", "employment_date", "salary", "major", "username"]:
                    culomns.append(promptSession.prompt(input + ': '))
                id = appSession.create_user(culomns)
            elif type_of_user == "nurse":
                culomns = []
                for input in ["firstname", "lastname", "national_code", "sexual", "birthday", "maried", "section", "employee_id", "employment_date", "salary", "username"]:
                    culomns.append(promptSession.prompt(input + ': '))
                id = appSession.create_user(culomns)
            elif type_of_user == "employee":
                culomns = []
                for input in ["firstname", "lastname", "national_code", "sexual", "birthday", "maried", "section", "employee_id", "employment_date", "salary", "carrer", "username"]:
                    culomns.append(promptSession.prompt(input + ': '))
                id = appSession.create_user(culomns)
            elif type_of_user == "patient":
                culomns = []
                for input in ["firstname", "lastname", "national_code", "sexual", "birthday", "maried", "section", "patient_type", "drugs", "username", "doctor_username", "nurse_username"]:
                    culomns.append(promptSession.prompt(input + ': '))
                id = appSession.create_user(culomns)
            appSession.assign_user_relation_id(id, username)
        elif command == 'update-access':
            print('Your Privacy')
        elif command == 'remove-user':
            print('Your Privacy')
        else:
            colnames, result = appSession.query(command)
            result.insert(0, colnames)
            table = AsciiTable(result)
            print(table.table)
