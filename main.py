from menu import main_menu, book_menu, user_menu, author_menu, genre_menu
from book import Book
from user import User
from author import Author
from genre import Genre

def handle_book_menu():
    choice = input("Enter your choice: ")
    if choice == "1":
        add_book()
    elif choice == "2":
        borrow_book()
    elif choice == "3":
        return_book()
    elif choice == "4":
        search_book()
    elif choice == "5":
        display_all_books()
    else:
        print("Invalid choice. Please try again.")

def add_book():
    title = input("Enter the title of the book: ")
    author_id = input("Enter the ID of the author: ")
    genre_id = input("Enter the ID of the genre: ")
    isbn = input("Enter the ISBN of the book: ")
    publication_date = input("Enter the publication date (YYYY-MM-DD): ")
    
    new_book = Book(title, author_id, genre_id, isbn, publication_date)
    
    try:
        new_book.add_book()
        print("Book added successfully!")
    except Exception as e:
        print("Error:", e)

def borrow_book():
    book_id = input("Enter the ID of the book you want to borrow: ")
    user_id = input("Enter your user ID: ")

    try:
        Book.borrow_book(book_id, user_id)
        print("Book borrowed successfully!")
    except Exception as e:
        print("Error:", e)

def return_book():
    book_id = input("Enter the ID of the book you want to return: ")

    try:
        Book.return_book(book_id)
        print("Book returned successfully!")
    except Exception as e:
        print("Error:", e)

def search_book():
    query = input("Enter search query (title, author, genre, etc.): ")

    results = Book.search_book(query)
    if results:
        print("Search results:")
        for book in results:
            print(book)
    else:
        print("No books found.")

def display_all_books():
    all_books = Book.display_all_books()
    if all_books:
        print("All Books:")
        for book in all_books:
            print(book)
    else:
        print("No books found.")

def handle_user_menu():
    user_choice = input("Enter your choice: ")
    if user_choice == "1":
        add_user()
    elif user_choice == "2":
        view_user_details()
    elif user_choice == "3":
        display_all_users()
    else:
        print("Invalid choice. Please try again.")

def add_user():
    name = input("Enter the name of the user: ")
    library_id = input("Enter the library ID of the user: ")

    new_user = User(name, library_id)

    try:
        new_user.add_user()
        print("User added successfully!")
    except Exception as e:
        print("Error:", e)

def view_user_details():
    user_id = input("Enter the ID of the user: ")

    user_details = User.view_user_details(user_id)
    if user_details:
        print("User Details:")
        print(user_details)
    else:
        print("User not found.")

def display_all_users():
    all_users = User.display_all_users()
    if all_users:
        print("All Users:")
        for user in all_users:
            print(user)
    else:
        print("No users found.")

def handle_author_menu():
    while True:
        author_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            add_author()
        elif choice == "2":
            view_author_details()
        elif choice == "3":
            display_all_authors()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

def add_author():
    name = input("Enter the name of the author: ")
    biography = input("Enter the biography of the author: ")

    new_author = Author(name, biography)

    try:
        new_author.add_author()
        print("Author added successfully!")
    except Exception as e:
        print("Error:", e)

def view_author_details():
    author_id = input("Enter the ID of the author: ")

    author_details = Author.view_author_details(author_id)
    if author_details:
        print("Author Details:")
        print(author_details)
    else:
        print("Author not found.")

def display_all_authors():
    all_authors = Author.display_all_authors()
    if all_authors:
        print("All Authors:")
        for author in all_authors:
            print(author)
    else:
        print("No authors found.")

def handle_genre_menu():
    pass

def main():
    while True:
        main_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            book_menu()
            handle_book_menu()
        elif choice == "2":
            user_menu()
            handle_user_menu()
        elif choice == "3":
            author_menu()
            handle_author_menu()
        elif choice == "4":
            genre_menu()
            handle_genre_menu()
        elif choice == "5":
            print("Thank you for using the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()