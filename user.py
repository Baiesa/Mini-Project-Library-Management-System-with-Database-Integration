from database import Database

class User:
    def __init__(self, name, library_id):
        self.name = name
        self.library_id = library_id

    @staticmethod
    def add_user(name, library_id):
        db = Database(host='127.0.0.1', user='root', password='Ameer@12345', database='library')
        query = "INSERT INTO users (name, library_id) VALUES (%s, %s)"
        values = (name, library_id)

        try:
            db.execute_statement(query, values)
        except Exception as e:
            raise e

    @staticmethod
    def view_user_details(user_id):
        db = Database(host='127.0.0.1', user='root', password='Ameer@12345', database='library')
        query = "SELECT * FROM users WHERE id = %s"
        values = (user_id,)

        try:
            result = db.execute_query(query, values)
            if result:
                return result[0]  
            else:
                return None
        except Exception as e:
            raise e

    @staticmethod
    def display_all_users():
        db = Database(host='127.0.0.1', user='root', password='Ameer@12345', database='library')
        query = "SELECT * FROM users"

        try:
            result = db.execute_query(query)
            return result
        except Exception as e:
            raise e