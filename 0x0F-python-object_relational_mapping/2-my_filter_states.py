#!/usr/bin/python3
'''A script that lists all states with a name starting with Nfrom the database hbtn_0e_0_usa'''
if __name__ == "__main__":
    import sys
    import MySQLdb

    #declaring some variable and initialise them with the arguments
    Cuser = sys.argv[1]
    passw = sys.argv[2]
    ourdb = sys.argv[3]
    my_host = 'localhost'
    my_p = 3306
    cname = sys.argv[4]

    #establishing the connection
    ourdb = MySQLdb.connect(host=my_host, user=Cuser, passwd=passw, db=ourdb, port=my_p)

    #creating cursor
    The_cursor = ourdb.cursor()

    #executing the query
    qer = "SELECT * from states WHERE name LIKE '{}' ORDER BY states.id ASC".format(cname)
    The_cursor.execute(qer)

    # retriving the answer
    result = The_cursor.fetchall()

    #printing the result
    for city in result:
        print(city)

    #closing corsor And the connection object
    The_cursor.close()
    ourdb.close()
