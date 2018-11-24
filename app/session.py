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

    def schema(self):
        self.cursor.execute("""SELECT table_name FROM information_schema.tables
            WHERE table_schema = 'public'""")
        tables = [x[0] for x in self.cursor.fetchall()]
        columns = []
        for table in tables:
            self.cursor.execute("""
            SELECT pg_attribute.attname 
            FROM 
                pg_index, pg_class, pg_attribute, pg_namespace 
            WHERE 
                pg_class.oid = '%s'::regclass AND 
                indrelid = pg_class.oid AND 
                nspname = 'public' AND 
                pg_class.relnamespace = pg_namespace.oid AND 
                pg_attribute.attrelid = pg_class.oid AND 
                pg_attribute.attnum = any(pg_index.indkey) AND 
                indisprimary
            """ % (table))
            key = self.cursor.fetchone()[0]
            # schema.append()
            self.cursor.execute(
                """ select column_name from information_schema.columns where table_name = '%s' """ % (table))
            columns.append([x[0].replace(key, key + " - Primary Key") if x[0] == key else x[0]
                            for x in self.cursor.fetchall()])
        return tables, columns

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
        self.__query__(
            """ UPDATE "person" SET id = %s WHERE username = %s; """, (id, username))

    def delete_user(self, username):
        self.__query__(
            """ DELETE FROM "person" WHERE username = %s; """, (username, ))

    def close_connections(self):
        self.connection.close()
        self.cursor.close()
