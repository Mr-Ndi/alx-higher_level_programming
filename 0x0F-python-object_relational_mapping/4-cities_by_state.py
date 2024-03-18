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

    if len(sys.argv) != 4:
        sys.exit(1)

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
    my_cursor.execute("SELECT * FROM cities ORDER BY cities.id ASC;")

    # fetch all the data returned by the query and print each row
    my_data = my_cursor.fetchall()
    for row in my_data:
        print(row)

    # Close all cursors &  databases
    my_cursor.close()
    my_db.close()
