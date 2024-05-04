import mysql.connector

class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()

    def disconnect(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()

    def execute_query(self, query, values=None):
        self.connect()
        if values:
            self.cursor.execute(query, values)
        else:
            self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.disconnect()
        return result

    def execute_statement(self, statement, values=None):
        self.connect()
        if values:
            self.cursor.execute(statement, values)
        else:
            self.cursor.execute(statement)
        self.connection.commit()
        self.disconnect()