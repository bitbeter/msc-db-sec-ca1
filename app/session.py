import logging
import psycopg2
from app.utils import config

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

SQL_COMMANDS = {
    "login": """SELECT * FROM person WHERE username=%s AND password=%s""",  # Username and Password checking
}


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
        self.username = username
        self.passwrod = passwrod
        self.__login__()

    # @todo Mazaheri
    # @todo prevent from sql injection
    def query(self, query, param):
        """ Run query on database and return valus. We assume we have valid query """
        # cur = self.connection.cursor()
        # cur.execute(query, param)
        pass

    def __login__(self):
        # Check username and password
        cur = self.connection.cursor()
        # @todo prevent from sql injection
        cur.execute(SQL_COMMANDS["login"], (self.username, self.passwrod))
        row = cur.fetchone()
        if (row is not None) and (row[0] == self.username and row[1] == self.passwrod):
            logger.info("User %s sign in into app successfully" %
                        self.username)
        else:
            raise ValueError("Your username or password not correct")
