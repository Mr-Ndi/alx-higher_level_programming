#!/usr/bin/python3
"""
iporting python3
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    # declaring varables
    my_host = 'localhost'
    users = sys.argv[1]
    my_password = sys.argv[2]
    my_db = sys.argv[3]
    port = 3306

    # connect the db
    database = MySQLdb.connect(
            host=my_host, user=users, passwd=my_password, db=my_db, port=port
            )
    # create the cusror && execute the query
    corse = database.cursor()
    # executing the query
    corse.execute("SELECT * FROM states WHERE name \
LIKE BINARY 'N%' ORDER BY id ASC")

    # fetch the data queried
    my_data = corse.fetchall()

    # print a tuple
    for data in my_data:
        print(data)
    # closing the cursor
    corse.close()
    # closing the db
    database.close()