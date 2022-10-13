#!/usr/bin/env python3
import sqlite3
from sqlite3 import Error

# conn = sqlite3.connect('StoreDB')
# c = conn.cursor()
# c.execute("CREATE TABLE Store(idStore INT, SquareFeet INT, StoreType VARCHAR(45), LocationType VARCHAR(1), Address VARCHAR(45), City VARCHAR(45), StoreState VARCHAR(45), ZipCode VARCHAR(10));")

# c.execute("INSERT INTO Store VALUES(1, 200, 'standalone', 'F', '4604 S Swadley', 'Morrison', 'CO', '80465');")


# class DB:
#     def __init__(self, dbname='lbstore.db'):
#         conn = sqlite3.connect(dbname)
#         self.point = conn.cursor()
#         self.point.execute("CREATE TABLE Store(item VARCHAR(45), price INT);")
        
        

# lb_store = DB()


# def add_item(item, price):
#     lb_store.point.execute("INSERT INTO Store VALUES(?, ?);", (item, price))
#     display = lb_store.point.execute("SELECT * FROM Store;")
#     print(display.fetchone())
#     return lb_store



# def create_table(lindsay_db):
#     lindsay_db.c.execute("CREATE TABLE Animals VALUES(name VARCHAR(45), type VARCHAR(10), age INT);")
#     animals_db = lindsay_db.c.execute
#     return animals_db


# def create_connection(dbname):
#     conn = sqlite3.connect(dbname)
#     return conn

def create_table(conn, table_details):
    try:
        c = conn.cursor()
        c.execute(table_details)
    except Error as e:
        print(e)



dbname = "StoreDB.db"

store_table_details = "CREATE TABLE Store(id INT PRIMARY KEY, idStore INT, SquareFeet INT, StoreType VARCHAR(45), LocationType CHAR(1), Address VARCHAR(45), City VARCHAR(45), StoreState VARCHAR(45), ZipCode VARCHAR(10));"
store_product_table_details = "CREATE TABLE Store_Product(id INT PRIMARY KEY, ProductID INT, StoreID INT, Quantity INT);"
product_table_details = "CREATE TABLE Product(id INT PRIMARY KEY, idProduct INT, Name VARCHAR(30), Price DECIMAL, CategoryID INT, Description VARCHAR(90));"
category_table_details = "CREATE TABLE Category(id INT PRIMARY KEY, idCategory INT, Name VARCHAR(45), Description VARCHAR(90));"





def create(dbname):
    conn = sqlite3.connect(dbname)
    create_table(conn, store_table_details)
    create_table(conn, store_product_table_details)
    create_table(conn, product_table_details)
    create_table(conn, category_table_details)
    return 


def fill(dbname):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    categories = [(1, 1, 'food', 'food items'),(2, 2, 'clothing', 'pants, shirts, etc')]
    for (id, idCategory, Name, Description) in categories:
        c.execute("INSERT INTO Category VALUES(?, ?, ?, ?);", (id, idCategory, Name, Description))

    stores = [(1, 11, 100, 'G', 'C', '111 franklin st', 'CO', '88808'),(2, 22, 200, 'NG', 'S', '88 morrison rd', 'morrison', 'CO', '88801')]
    for (id, idStore, SquareFeet, StoreType, LocationType, Address, City, StoreState, ZipCode) in stores:
            c.execute("INSERT INTO Store VALUES(?, ?, ?, ?, ?, ?, ?, ?);", (id, idStore, SquareFeet, StoreType, LocationType, Address, City, StoreState, ZipCode))
