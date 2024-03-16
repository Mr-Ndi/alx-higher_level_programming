#!/usr/bin/python3
"""
Module that connects a python script to a database
"""

if __name__ == "__main__":

    import MySQLdb
    import sys

    # declaring the vars
    my_host = 'localhost'
    users = sys.argv[1]
    my_password = sys.argv[2]
    my_db = sys.argv[3]
    port = 3306
    # Connect database using command-line arguments
    my_db = MySQLdb.connect(
            host=my_host, user=users, passwd=my_password, db=my_db, port=port
            )
    # Create cursor obj to interact with database
    my_cursor = my_db.cursor()

    # Execute a SELECT query to fetch data
    my_cursor.execute("SELECT * FROM states ORDER BY states.id ASC;")

    # fetch all the data returned by the query
    my_data = my_cursor.fetchall()

    # Iterate through the fetched data and print each row
    for row in my_data:
        print(row)

    # Close all cursors
    my_cursor.close()

    # Close all databases
    my_db.close()
