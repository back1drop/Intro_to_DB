import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="password"
)
mycursor=mydb.cursor()
try:
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")
except:
    print("ERROR failed to connect")

mycursor.execute("USE alx_book_store")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS Authors(
    author_id INT AUTO_INCREMENT PRIMARY KEY,
    author_name VARCHAR(215)
)
""")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS Books(
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(130),
    author_id INT,
    price DOUBLE,
    publication_date DATE,
    FOREIGN KEY(author_id) REFERENCES Authors(author_id) 
)
""")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS Customers(
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(215),
    email VARCHAR(215),
    address TEXT
)
""")
mycursor.execute("""
CREATE TABLE IF NOT EXISTS Orders(
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    FOREIGN KEY(customer_id) REFERENCES Customers(customer_id)    
)
""")
mycursor.execute("""
CREATE TABLE IF NOT EXISTS Order_Details(
    orderdetailid INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    book_id INT,
    quantity DOUBLE,
    FOREIGN KEY(order_id) REFERENCES Orders(order_id),
    FOREIGN KEY(book_id) REFERENCES Books(book_id)  
)
""")
print("Tables Created")

"""information_schema is a special built-in database that stores metadata """
mycursor.execute("""
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'alx_book_store'
    """)
mytables=mycursor.fetchall()
for table in mytables:
    print(table[0])#use zero to return only the string and not the tuple
mycursor.close()
mydb.close()