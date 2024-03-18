#!/usr/bin/python3
'''
A script that takes in arguments and
displays all values in the states table of hbtn_0e_0_usa
'''
if __name__ == "__main__":
    import sys
    import MySQLdb

    Cuser = sys.argv[1]
    passw = sys.argv[2]
    ourdb = sys.argv[3]
    my_host = 'localhost'
    my_p = 3306
    cname = sys.argv[4]

    ourdb = MySQLdb.connect(
        host=my_host, user=Cuser, passwd=passw, db=ourdb, port=my_p
        )
    The_cursor = ourdb.cursor()

    The_cursor.execute(
        """SELECT * FROM cities
        INNER JOIN states
        ON cities.state_id = states.id
        ORDER BY cities.id"""
    )

    print(", ".join([city[2]
                     for city in The_cursor.fetchall()
                     if city[4] == sys.argv[4]])

          )

    The_cursor.close()
    ourdb.close()
