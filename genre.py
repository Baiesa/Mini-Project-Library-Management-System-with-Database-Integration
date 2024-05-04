from database import Database

class Genre:
    def __init__(self, name, description, category):
        self.name = name
        self.description = description
        self.category = category

    @staticmethod
    def add_genre(name, description, category):
        db = Database(host='127.0.0.1', user='root', password='Ameer@12345', database='library')
        query = "INSERT INTO genres (name, description, category) VALUES (%s, %s, %s)"
        values = (name, description, category)

        try:
            db.execute_statement(query, values)
        except Exception as e:
            raise e

    @staticmethod
    def view_genre_details(genre_id):
        db = Database(host='127.0.0.1', user='root', password='Ameer@12345', database='library')
        query = "SELECT * FROM genres WHERE id = %s"
        values = (genre_id,)

        try:
            result = db.execute_query(query, values)
            if result:
                return result[0]  
            else:
                return None
        except Exception as e:
            raise e

    @staticmethod
    def display_all_genres():
        db = Database(host='127.0.0.1', user='root', password='Ameer@12345', database='library')
        query = "SELECT * FROM genres"

        try:
            result = db.execute_query(query)
            return result
        except Exception as e:
            raise e