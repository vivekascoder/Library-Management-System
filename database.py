import sqlite3 as sql

con = sql.connect('db.sqlite3')
cur = con.cursor()

books_table = """ CREATE TABLE books (
                id integer primary key autoincrement,
                name char(40) not null,
                author char(40) not null,
                publisher char(40) not null,
                price integer not null,
                image BLOB not null
                ) """

issued_table = """CREATE TABLE issued (
                id integer primary key autoincrement,
                name char(40) not null,
                phone char(13) not null,
                book_id integer not null,
                book_name char(40) not null
                )"""

users_table = """ CREATE TABLE users (
                id integer primary key not null,
                username char(40) not null,
                password char(40) not null
                )"""

insert_book = """INSERT INTO books
                (name, author, publisher, price, image)
                VALUES (?, ?, ?, ?, ?)"""

insert_issued = """INSERT INTO issued
                (name, phone, book_id, book_name)
                VALUES (?, ?, ?, ?) """

insert_user = """INSERT INTO users (username, password)
                VALUES (?, ?)"""


def createTable(query):
    cur.execute(query)
    print("Table Created.")

def insertBook(data):
    cur.execute(insert_book, data)
    con.commit()
    print("Inserted: ", data)

def insertIssued(data):
    cur.execute(insert_issued, data)
    con.commit()
    print("Inserted: ", data)

def insertUser(data):
    cur.execute(insert_user, data)
    con.commit()
    print("Inserted: ", data)

def toBinary(file_name):
    file = open(file_name, 'rb')
    blob = file.read()
    return blob

def validateUser(username, password):
    query = """ select  password from users where username=? """
    cur.execute(query, (username, ))
    try:
        if cur.fetchone()[0]==password:
            return True
        else:
            return False
    except:
        return False

##createTable(books_table)
##createTable(users_table)
