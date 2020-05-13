import sqlite3
from sqlite3 import Error


def choice():
    print("""
    Put 1 to pull up the customer menu,
    2 for the books menu,
    3 to pull up the orders,
    4 to exit code. 
    """)
    answer = int(input(">"))
    while answer <= 1 >= 3:         # Unlimited loop for the menu
        choice()
    if answer == 1:
        customer_menu()
    if answer == 2:
        books_menu()
    if answer == 3:
        order_menu()
    else:
        if answer == 4:
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
    while answer <= 1 >= 5:     # Unlimited loop for the menu
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
        execute_query(connection, create_customer)      # executes the query
        print("Here is the customer table")
        select_customers = "SELECT * from customer"
        people = execute_read_query(connection, select_customers)       # executes the query
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
        execute_query(connection, update_customer)      # executes the query
        print("Whos last name was 'Suter' is now 'magee'")
        return choice()
    if answer == 3:
        print("Here is the customer table")
        select_customers = "SELECT * from customer"
        people = execute_read_query(connection, select_customers)       # executes the query
        for person in people:
            print(person)
        return choice()
    if answer == 4:
        delete_book = """(
        DELETE FROM customer
        WHERE last_name = "magee"
        );"""
        execute_query(connection, delete_book)      # executes the query
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
    while answer <= 1 >= 5:     # Unlimited loop for the menu
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
        execute_query(connection, create_book)      # executes the query
        print("Here is the books table")
        select_book = "SELECT * from books"
        books = execute_read_query(connection, select_book)     # executes the query
        for book in books:          # this goes through the table printing each row of data
            print(book)
        return choice()
    if answer == 2:
        update_book = """ (
        UPDATE books
        SET title = "magee"
        WHERE title = "fire"
        );
        """
        execute_query(connection, update_book)      # executes the query
        print("Who's title was 'fire' is now 'magee'")
        return choice()
    if answer == 3:
        print("Here is the books table")
        select_book = "SELECT * from books"
        books = execute_read_query(connection, select_book)     # executes the query
        for book in books:
            print(book)
        return choice()
    if answer == 4:
        delete_book = """(
        DELETE FROM books
        WHERE title = "magee"
        );"""
        execute_query(connection, delete_book)      # executes the query
        print("You just deleted any book with the title 'magee'")
        return choice()
    else:
        if answer == 5:
            choice()


def order_menu():
    print("""
    Enter 1 to place an order,
    Enter 2 to view the orders submitted,
    Enter 3 to view more information about the submitted orders,
    Enter 4 to return to the main menu
    """)
    answer = int(input(">"))
    while answer <= 1 >= 5:         # Unlimited loop for the menu
        order_menu()
    if answer == 1:
        print("Please enter the following information about the order being recorded.")
        order_date = input("Enter the date this was ordered in this format '09/12/01'..>")
        order_cost = input("Enter the total cost of this order..>")
        quantity = input("Enter the number of books ordered..>")
        create_order = f"""
        INSERT INTO
            orders (order_date, order_total)
        VALUES
        ('{order_date}', '{order_cost}');
        """
        execute_query(connection, create_order)     # executes the query
        create_orderlineitem = f"""
        INSERT INTO 
            orderlineitem (quantity)
        VALUES
        ('{quantity}');
        """
        execute_query(connection, create_orderlineitem)     # executes the query
        print("Here is the newly updated orders table")
        print("The following table appears like so (Order#, Order date, Cost per book, Customer_id)")
        select_order = "SELECT * from orders"
        orders = execute_read_query(connection, select_order)        # executes the query
        for order in orders:
            print(order)
        return choice()
    if answer == 2:
        print("Here is the newly updated orders table")
        print("The following table appears like so (Order#, Order date, Cost per book, Customer_id")
        select_order = "SELECT * from orders"
        orders = execute_read_query(connection, select_order)        # executes the query
        for order in orders:
            print(order)
        return choice()
    if answer == 3:
        print("Here is the advanced information table")
        print("The following table appears like so (Order_id, book_id, quantity of books ordered)")
        select_order = "SELECT * from orderlineitem"
        orders = execute_read_query(connection, select_order)       # executes the query
        for order in orders:
            print(order)
        return choice()
    if answer == 4:
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
connection = create_connection("Assignment13.db")       # executes the query


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


create_order_table = """
CREATE TABLE IF NOT EXISTS orders (
    order_number INTEGER PRIMARY KEY AUTOINCREMENT,
    order_date TEXT NOT NULL,
    order_total TEXT NOT NULL,
    customer_id INTEGER AUTOINCREMENT,
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
);
"""

create_orderlineitem_table = """
CREATE TABLE IF NOT EXISTS orderlineitem (
    order_number INTEGER AUTOINCREMENT,
    book_id INTEGER AUTOINCREMENT,
    quantity TEXT NOT NULL,
    PRIMARY KEY (order_number, book_id),
    FOREIGN KEY (order_number) REFERENCES orders(order_number)
    FOREIGN KEY (book_id) REFERENCES books(book_id)
);
"""

create_customer_table = """
CREATE TABLE IF NOT EXISTS customer (
  customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
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
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
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
execute_query(connection, create_order_table)
execute_query(connection, create_orderlineitem_table)

choice()
