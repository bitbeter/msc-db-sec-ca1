import sys
import getpass
from app.session import Session
from app.sql_parser import SQLParser
from app.sql_commands import SQL_COMMANDS
from app.utils import Color
from prompt_toolkit import prompt
from prompt_toolkit import PromptSession
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.shortcuts import yes_no_dialog
from pygments.lexers.sql import SqlLexer
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.lexers import PygmentsLexer
from terminaltables import SingleTable

HELP_MESSAGE = """{0}Avalibale Commands:
{1}exit          {3}Exit the app
{1}<query>       {3}Select, Insert and Update
{1}my privacy    {3}Show all other users access to my information {2}check it now{3}""".format(Color.CYAN, Color.BLUE, Color.REVERSE, Color.RESET)


WORDS = [
    # Commands
    'EXIT', 'MY PRIVACY',
    'CREATE USER', 'DELETE USER',
    # Query Keywords
    'SELECT', 'INSERT INTO',
    'WHERE',  'UPDATE', 'FROM', 'SET', 'VALUES',
    'AND', 'OR', 'NOT',
]


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
    # return Session('admin', 'admin')


def shell(yes_to_all=False):
    global WORDS
    promptSession = PromptSession(
        lexer=PygmentsLexer(SqlLexer), auto_suggest=AutoSuggestFromHistory()
    )
    appSession = None
    while (True):
        try:
            appSession = login()
            break
        except ValueError as error:
            print(error)
    tables, culomns = appSession.schema()
    fields = {}
    for i in range(len(tables)):
        fields[tables[i]] = culomns[i]
        WORDS.append(tables[i])
        WORDS = WORDS + culomns[i]
        singleTable = SingleTable(
            [culomns[i][x:x+5] for x in range(0, len(culomns[i]), 5)], title=tables[i])
        singleTable.inner_row_border = True
        print(singleTable.table)
    WORDS = list(set(WORDS))
    WORDS.sort()

    while (True):
        command = promptSession.prompt(
            '> ', completer=WordCompleter(WORDS, ignore_case=True)).lower()
        if command == '-h':
            print(HELP_MESSAGE)
        elif command == 'exit':
            if do_you_sure(yes_to_all):
                appSession.close_connections()
                sys.exit()
        elif command == 'my privacy':
            print('Your Privacy')
        elif command == 'create user':
            p = fields["person"].copy()
            p.remove('id')
            i = []
            t = None
            username = None
            for input in p:
                ans = promptSession.prompt(input + " : ")
                while ans is None or ans == "":
                    ans = promptSession.prompt(input + " : ")
                if input == 'type':
                    t = ans
                if input == 'username':
                    username = ans
                i.append(ans)
            appSession.create_user(p, i)
            obj_items = fields[t].copy()
            obj_items.remove('id')
            obj_items.remove('username')
            i = []
            for input in obj_items:
                i.append(promptSession.prompt(input + " : "))
            obj_items.append('username')
            i.append(username)
            id = appSession.create_obj(t, obj_items, i)
            appSession.assign_user_relation_id(id, username)
        elif command == 'delete user':
            username = promptSession.prompt('Username: ').lower()
            appSession.delete_user(username)
        else:
            # sql = "select * from person"
            # sql = "select sum() from doctor"
            # sql = "delete from person where username='hasan' and password='jasem'"
            # sql = "update person set username='hasan' where a > 20"
            # sql = "insert into person (username, password) VALUES (1, 0), (2,0);"
            # sql = "insert into person(username, password) VALUES (1, 0);"
            # print(sql)
            # print(SQLParser.parse_sql_columns(sql))
            # print(SQLParser.parse_sql_tables(sql))

            # SQLParser.parse(sql)
            colnames, result = appSession.query(command)
            result.insert(0, colnames)
            table = SingleTable(result)
            print(table.table)
