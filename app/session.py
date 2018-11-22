from app.utils import config
import psycopg2
db = psycopg2.connect(host="localhost", database="suppliers",
                      user="postgres", password="postgres")


def connect():
    """ Connect to the PostgreSQL database server and test connection """
    conn = None
    try:
        # read connection parameters
        params = config(filename='/sql/database.ini', section='postgresql')

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        # close the communication with the PostgreSQL
        cur.close()
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return None


class Session():
    def __init__(self, username, passwrod):
        self.username = username
        self.passwrod = passwrod
        self.connection = connect()

    # @todo Mazaheri
    def query(self, session_id, query):
        """ Run query on databse and return valus. We assume we have valid query """
        pass
