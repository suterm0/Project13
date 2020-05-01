import sqlite3
from sqlite3 import Error


def choice():
    print("""
    Put 1 to pull up the customer menu,
    2 for the books menu,
    3 to exit code. 
    """)
    answer = int(input(">"))
    while answer <= 1 >= 3:
        choice()
    if answer == 1:
        customer_menu()
    if answer == 2:
        books_menu()
    else:
        if answer == 3:
            exit("goodbye")


def customer_menu():
    print("""
    1 to add to the customer table
    2 to modify a customers name
    3 to print the customers table
    4 to delete a customer
    5 to return to the main menu
    """)
    answer = int(input(">"))
    while answer <= 1 >= 5:
        customer_menu()
    if answer == 1:
        print("Please enter the details for the person:")
        first_name = input("What is the first name?")
        last_name = input("What is the last name?")
        street_address = input("What is the street address?")
        city = input("What is the city?")
        state = input("What is the state?")
        zip_code = input("What is the zip code?")
        create_customer = f"""
        INSERT INTO
            customer (first, last, address, city, state, zip)
        VALUES
        ('{first_name}', '{last_name}', '{street_address}', '{city}', '{state}', '{zip_code}');
        """
        execute_query(connection, create_customer)
        print("Here is the customer table")
        select_customers = "SELECT * from customer"
        people = execute_read_query(connection, select_customers)
        for person in people:
            print(person)
            return choice()
    if answer == 2:
        update_customer = """ (
        UPDATE customer
        SET last_name = "magee"
        WHERE last_name = "suter"
        );
        """
        execute_query(connection, update_customer)
        print("Whos last name was 'Suter' is now 'magee'")
        return choice()
    if answer == 3:
        print("Here is the customer table")
        select_customers = "SELECT * from customer"
        people = execute_read_query(connection, select_customers)
        for person in people:
            print(person)
        return choice()
    if answer == 4:
        delete_book = """(
        DELETE FROM customer
        WHERE last_name = "magee"
        );"""
        execute_query(connection, delete_book)
        print("You just deleted any person with the last name 'magee'")
        return choice()
    else:
        if answer == 5:
            choice()


def books_menu():
    print("""
    1 to add to the books table
    2 to modify a book
    3 to print the books table
    4 to delete a book
    5 to return to the main menu
    """)
    answer = int(input(">"))
    while answer <= 1 >= 5:
        customer_menu()
    if answer == 1:
        print("Please enter the following information to add a book to the table")
        title= input("What is the title?")
        author = input("Who is the author?")
        isbn = input("What is the ISBN?")
        edition = input("What is edition?")
        price = input("What is the price?")
        publisher = input("Who is the publisher?")
        create_book = f"""
        INSERT INTO
            books (title, author, isbn, edition, price, publisher)
        VALUES
        ('{title}', '{author}', '{isbn}', '{edition}', '{price}', '{publisher}');
        """
        execute_query(connection, create_book)
        print("Here is the books table")
        select_book = "SELECT * from books"
        books = execute_read_query(connection, select_book)
        for book in books:
            print(book)
            return choice()
    if answer == 2:
        update_book = """ (
        UPDATE books
        SET title = "magee"
        WHERE title = "fire"
        );
        """
        execute_query(connection, update_book)
        print("Who's title was 'fire' is now 'magee'")
        return choice()
    if answer == 3:
        print("Here is the books table")
        select_book = "SELECT * from books"
        books = execute_read_query(connection, select_book)
        for book in books:
            print(book)
            return choice()
    if answer == 4:
        delete_book = """(
        DELETE FROM books
        WHERE title = "magee"
        );"""
        execute_query(connection, delete_book)
        print("You just deleted any book with the title 'magee'")
        return choice()
    else:
        if answer == 5:
            choice()


def create_connection(path):
    conn = None
    try:
        conn = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return conn

print("Connect to SQLite database:")
connection = create_connection("Assignment13.db")


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")



create_customer_table = """
CREATE TABLE IF NOT EXISTS customer (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  first TEXT NOT NULL,
  last TEXT NOT NULL,
  address TEXT NOT NULL,
  city TEXT NOT NULL,
  state TEXT NOT NULL,
  zip TEXT NOT NULL
);
"""

create_books_table = """
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  author TEXT NOT NULL,
  ISBN TEXT NOT NULL,
  edition TEXT NOT NULL,
  state TEXT NOT NULL,
  zip TEXT NOT NULL
);
"""

print("\nRun the query to create the customer table:")
execute_query(connection, create_customer_table)
execute_query(connection, create_books_table)


choice()
