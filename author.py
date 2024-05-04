from database import Database

class Author:
    def __init__(self, name, biography):
        self.name = name
        self.biography = biography

    @staticmethod
    def add_author(name, biography):
        db = Database(host='127.0.0.1', user='root', password='Ameer@12345', database='library')
        query = "INSERT INTO authors (name, biography) VALUES (%s, %s)"
        values = (name, biography)

        try:
            db.execute_statement(query, values)
        except Exception as e:
            raise e

    @staticmethod
    def view_author_details(author_id):
        db = Database(host='127.0.0.1', user='root', password='Ameer@12345', database='library')
        query = "SELECT * FROM authors WHERE id = %s"
        values = (author_id,)

        try:
            result = db.execute_query(query, values)
            if result:
                return result[0] 
            else:
                return None
        except Exception as e:
            raise e

    @staticmethod
    def display_all_authors():
        db = Database(host='127.0.0.1', user='root', password='Ameer@12345', database='library')
        query = "SELECT * FROM authors"

        try:
            result = db.execute_query(query)
            return result
        except Exception as e:
            raise e