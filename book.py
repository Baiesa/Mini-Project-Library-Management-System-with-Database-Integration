from database import Database

class Book:
    def __init__(self, title, author_id, genre_id, isbn, publication_date):
        self.title = title
        self.author_id = author_id
        self.genre_id = genre_id
        self.isbn = isbn
        self.publication_date = publication_date

    @staticmethod
    def add_book(title, author_id, genre_id, isbn, publication_date):
        db = Database(host='127.0.0.1', user='root', password='Ameer@12345', database='library')
        query = "INSERT INTO books (title, author_id, genre_id, isbn, publication_date) VALUES (%s, %s, %s, %s, %s)"
        values = (title, author_id, genre_id, isbn, publication_date)

        try:
            db.execute_statement(query, values)
        except Exception as e:
            raise e

    @staticmethod
    def borrow_book(book_id, user_id):
        db = Database(host='127.0.0.1', user='root', password='Ameer@12345', database='library')
        borrow_date = "2024-05-05"  
        query = "INSERT INTO borrowed_books (user_id, book_id, borrow_date) VALUES (%s, %s, %s)"
        values = (user_id, book_id, borrow_date)

        try:
            db.execute_statement(query, values)
           
        except Exception as e:
            raise e

    @staticmethod
    def return_book(book_id):
        db = Database(host='127.0.0.1', user='root', password='Ameer@12345', database='library')
        return_date = "2024-05-05"  
        query = "UPDATE borrowed_books SET return_date = %s WHERE book_id = %s AND return_date IS NULL"
        values = (return_date, book_id)

        try:
            db.execute_statement(query, values)
            
        except Exception as e:
            raise e

    @staticmethod
    def search_book(query):
        db = Database(host='127.0.0.1', user='root', password='Ameer@12345', database='library')
        query = "SELECT * FROM books WHERE title LIKE %s OR isbn LIKE %s"  
        values = ('%' + query + '%', '%' + query + '%')

        try:
            result = db.execute_query(query, values)
            return result
        except Exception as e:
            raise e

    @staticmethod
    def display_all_books():
        db = Database(host='127.0.0.1', user='root', password='Ameer@12345', database='library')
        query = "SELECT * FROM books"

        try:
            result = db.execute_query(query)
            return result
        except Exception as e:
            raise e