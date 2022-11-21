<<<<<<< HEAD
import psycopg2


class PostgresConnection(object):
    def __init__(self):
        self.connection = psycopg2.connect(database="ecomdb",
                                           user="postgres",
                                           password="mudabbir",
                                           host="127.0.0.1",
                                           port="5432")

    def getConnection(self):
        print("successfully connected to database")
=======
import psycopg2


class PostgresConnection(object):
    def __init__(self):
        self.connection = psycopg2.connect(database="ecomdb",
                                           user="postgres",
                                           password="mudabbir",
                                           host="127.0.0.1",
                                           port="5432")

    def getConnection(self):
        print("successfully connected to database")
>>>>>>> 1f7bc4e1f0325aa32c9be9cdbfcfbf71eb1cee42
        return self.connection