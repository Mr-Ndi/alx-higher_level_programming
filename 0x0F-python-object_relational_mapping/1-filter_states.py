#!/usr/bin/python3
"""
importing python3
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    # connect the db
    database = MySQLdb.connect(
            user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3]
            )
    # create the cusror && execute the query
    c = db.cursor()
    # executing the query
    c.execute("SELECT * FROM states ORDER BY id ASC")

    # print a tuple
    [print(data) for data in c.fetchall() if data[1][0] == "N"]
    # closing the cursor
    c.close()
    # closing the db
    database.close()
