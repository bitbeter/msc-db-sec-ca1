import logging
import psycopg2
from app.utils import config
from app.sql_commands import SQL_COMMANDS

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def connect():
    """ Connect to the PostgreSQL database server and test connection """
    conn = None
    try:
        # read connection parameters
        params = config(filename='./configs/database.ini',
                        section='postgresql')

        # connect to the PostgreSQL server
        logger.info('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        logger.debug('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        logger.debug(db_version)

        # close the communication with the PostgreSQL
        cur.close()
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return None


class Session():
    def __init__(self, username, passwrod):
        self.connection = connect()
        self.cursor = self.connection.cursor()
        self.username = username
        self.passwrod = passwrod
        self.__login__()

    def __query__(self, sql, params):
        cur = self.connection.cursor()
        cur.execute(sql, params)
        # result = [list(row) for row in cur.fetchall()]
        # colnames = [desc[0] for desc in cur.description]
        # cur.close()
        # return colnames, result

    def __login__(self):
        # Check username and password
        cur = self.connection.cursor()
        # @todo prevent from sql injection
        cur.execute(SQL_COMMANDS["login"], (self.username, self.passwrod))
        row = cur.fetchone()
        cur.close()
        if (row is not None) and (row[0] == self.username and row[1] == self.passwrod):
            logger.info("User %s sign in into app successfully" %
                        self.username)
        else:
            raise ValueError("Your username or password not correct")

    # @todo Mazaheri
    # @todo prevent from sql injection
    def query(self, query, params=None):
        """ Run query on database and return values. We assume we have valid query """
        cur = self.connection.cursor()
        cur.execute(query, params)
        result = [list(row) for row in cur.fetchall()]
        colnames = [desc[0] for desc in cur.description]
        cur.close()
        return colnames, result

    def create_user(self, params):
        self.__query__(SQL_COMMANDS["create-user"], params)

    def create_doctor(self, params):
        self.__query__(SQL_COMMANDS["create-doctor"], params)
        id = self.cursor.fetchone()
        return id

    def create_nurse(self, params):
        self.__query__(SQL_COMMANDS["create-nurse"], params)
        id = self.cursor.fetchone()
        return id

    def create_patient(self, params):
        self.__query__(SQL_COMMANDS["create-patient"], params)
        id = self.cursor.fetchone()
        return id

    def create_employee(self, params):
        self.__query__(SQL_COMMANDS["create-employee"], params)
        id = self.cursor.fetchone()
        return id

    def update_user_access(self):
        pass

    def assign_user_relation_id(self, id, username):
        self.__query__(SQL_COMMANDS["assign-user-relation-id"], (id, username))

    def delete_user(self, username):
        self.__query__(SQL_COMMANDS["delete-user"], (username))

    def close_connections(self):
        self.connection.close()
        self.cursor.close()
