#!/usr/bin/python3
'''A script that lists all states with a name with N '''
if __name__ == "__main__":
    import sys
    import MySQLdb

    #declaring some variable and initialise them with the arguments
    Cuser = sys.argv[1]
    passw = sys.argv[2]
    ourdb = sys.argv[3]
    my_host = 'localhost'
    my_p = 3306

    #establishing the connection
    ourdb = MySQLdb.connect(host=my_host, user=Cuser, passwd=passw, db=ourdb, port=my_p)

    #creating cursor
    _cursor = ourdb.cursor()

    #executing the query
    _cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    
    # retriving the answer
    result = _cursor.fetchall()

    #printing the result
    for city in result:
        print(city)

    #closing corsor And the connection object
    _cursor.close()
    ourdb.close()
