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

    question = "SELECT cities.name from cities JOIN\
          states ON cities.state_id=states.id WHERE states.name LIKE %s;"
    The_cursor.execute(question, (cname + '+%',))
    result = The_cursor.fetchall()

    for city in result:
        print(city)

    The_cursor.close()
    ourdb.close()
