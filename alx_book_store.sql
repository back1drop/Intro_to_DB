import mysql.connector

try:
    # Connect to MySQL Server
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password"  # replace with your actual password
    )

    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if 'mycursor' in locals():
        mycursor.close()
    if 'mydb' in locals() and mydb.is_connected():
        mydb.close()
