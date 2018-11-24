import sqlparse
from sqlparse.sql import IdentifierList, Identifier
from sqlparse.tokens import Keyword


class SQLParser(object):
    @staticmethod
    def parse_sql_columns(sql):
        columns = []
        parsed = sqlparse.parse(sql)
        stmt = parsed[0]
        for token in stmt.tokens:
            if isinstance(token, IdentifierList):
                for identifier in token.get_identifiers():
                    columns.append(identifier.get_real_name())
            if isinstance(token, Identifier):
                columns.append(token.get_real_name())
            if token.ttype is Keyword:  # from
                break
        return columns

    @staticmethod
    def get_table_name(token):
        parent_name = token.get_parent_name()
        real_name = token.get_real_name()
        if parent_name:
            return parent_name + "." + real_name
        else:
            return real_name

    @staticmethod
    def parse_sql_tables(sql):
        tables = []
        parsed = sqlparse.parse(sql)
        stmt = parsed[0]
        from_seen = False
        for token in stmt.tokens:
            if from_seen:
                if token.ttype is Keyword:
                    continue
                else:
                    if isinstance(token, IdentifierList):
                        for identifier in token.get_identifiers():
                            tables.append(SQLParser.get_table_name(identifier))
                    elif isinstance(token, Identifier):
                        tables.append(SQLParser.get_table_name(token))
                    else:
                        pass
            if token.ttype is Keyword and token.value.upper() == "FROM":
                from_seen = True
        return tables
