import mysql.connector

# Replace these values with your MySQL server's configuration
host = "localhost"
user = "root"
password = ""
database = "project1"

# Establish a connection to the MySQL server
try:
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    if connection.is_connected():
        print("Connected to MySQL")

    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Define the SQL query to create a table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS example_table (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        age INT
    )
    """

    # Execute the query to create the table
    cursor.execute(create_table_query)
    print("Table 'example_table' created successfully")

except mysql.connector.Error as error:
    print("Error:", error)

finally:
    # Close the cursor and connection
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")