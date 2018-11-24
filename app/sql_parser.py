import sqlparse
from sqlparse.sql import IdentifierList, Identifier, Where, TokenList
from sqlparse.tokens import Keyword, Whitespace, DML


class QueryTypes():
    SELECT = 'SELECT'
    DELETE = 'DELETE'
    UPDATE = 'UPDATE'
    INSERT = 'INSERT'


class QueryInfo():
    def __init__(self, type_, table, columns, conditions, assigments):
        self.type = type_
        self.table = table
        self.columns = columns
        self.conditions = conditions
        self.assigments = assigments


class SQLParser(object):
    @staticmethod
    def select(tokens):
        table = None
        columns = []
        conditions = []
        saveTableName = False
        saveColumns = True
        for token in tokens:
            if saveTableName:
                if isinstance(token, Identifier):
                    table = token.get_real_name()
                    saveTableName = False
            if saveColumns:
                if isinstance(token, Identifier):
                    columns.append(token.get_real_name())
                    saveColumns = False
                elif isinstance(token, IdentifierList):
                    for identifier in token.get_identifiers():
                        print(identifier)
                        columns.append(identifier.get_real_name())
                    saveColumns = False
            if token.ttype is Keyword and token.value.upper() == "FROM":
                saveTableName = True
                saveColumns = False
            if isinstance(token, Where):
                conditions = ''.join(
                    [token.value for token in token.tokens[1:]])
        print(table, columns, conditions)
        return table, columns, conditions

    @staticmethod
    def delete(tokens):
        table = None
        conditions = []
        for token in tokens:
            if isinstance(token, Identifier):
                table = token.get_real_name()
            if isinstance(token, Where):
                conditions = ''.join(
                    [token.value for token in token.tokens[2:]])
        print(table, conditions)
        return table, conditions

    @staticmethod
    def update(tokens):
        table = None
        assigments = []
        conditions = []
        isAfterSet = False
        for token in tokens:
            if not isAfterSet and isinstance(token, Identifier):
                table = token.get_real_name()
            if isAfterSet and not isinstance(token, Where):
                assigments = ''.join(
                    [token.value for token in token.tokens])
            if token.ttype is Keyword and token.value.upper() == "SET":
                isAfterSet = True
            if isinstance(token, Where):
                conditions = ''.join(
                    [token.value for token in token.tokens[2:]])
        print(table, conditions, assigments)
        return table, conditions, assigments

    @staticmethod
    def insert(tokens):
        table = None
        value_list = []
        values = []
        saveTableName = True
        for token in tokens:
            print(token)
            if saveTableName and isinstance(token, Identifier):
                table = token.get_real_name()
                saveTableName = False
            if saveTableName and isinstance(token, IdentifierList):
                tokenList = token.tokens
                table = tokenList[0].get_real_name()
                value_list = ''.join(
                    [token.value for token in tokenList[2:]])
                saveTableName = False
            if not saveTableName and not isinstance(token, Where):
                # assigments = ''.join(
                #     [token.value for token in token.tokens])
                print(token)
            # if isinstance(token, Where):
            #     conditions = ''.join(
            #         [token.value for token in token.tokens[2:]])
        print(table, value_list, values)
        return table, value_list, values

    @staticmethod
    def parse(sql):
        parsed = sqlparse.parse(sql)
        stmt = parsed[0]
        tokens = list(filter(lambda x: x.ttype != Whitespace, stmt.tokens))
        token = tokens[0]
        if token.ttype is DML:
            if token.value.upper() == QueryTypes.SELECT:
                table, columns, conditions = SQLParser.select(tokens)
                return QueryTypes.SELECT, table, columns, conditions
            elif token.value.upper() == QueryTypes.DELETE:
                table, conditions = SQLParser.delete(tokens)
                return QueryTypes.DELETE, table, conditions
            elif token.value.upper() == QueryTypes.UPDATE:
                table, conditions, assigments = SQLParser.update(tokens)
                return QueryTypes.UPDATE, table, conditions, assigments
            elif token.value.upper() == QueryTypes.INSERT:
                table, value_list, values = SQLParser.insert(tokens)
                return QueryTypes.INSERT, value_list, values
            else:
                return None
        else:
            return None
