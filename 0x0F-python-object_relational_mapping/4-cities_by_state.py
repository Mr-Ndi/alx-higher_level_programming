#!/usr/bin/python3
"""
Module that connects a python script to a database
"""

if __name__ == "__main__":
    """
    A script that lists all cities from the database
    """
    import MySQLdb
    import sys

    # Check if all required arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    # Extracting command-line arguments
    users = sys.argv[1]
    my_password = sys.argv[2]
    my_db = sys.argv[3]

    # Connect to the MySQL server
    my_db = MySQLdb.connect(
        host='localhost', user=users, passwd=my_password, db=my_db, port=3306
    )

    # Create a cursor object
    my_cursor = my_db.cursor()

    # Execute a SELECT query to fetch data
    my_cursor.execute("SELECT * FROM cities ORDER BY cities.id ASC;")

    # Fetch all the data returned by the query
    my_data = my_cursor.fetchall()

    # Display results as specified
    for row in my_data:
        print(row)

    # Close the cursor and database connection
    my_cursor.close()
    my_db.close()
