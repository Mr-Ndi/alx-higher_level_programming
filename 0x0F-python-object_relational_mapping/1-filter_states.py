#!/usr/bin/python3
'''
A script that lists all states with a name with N
'''
if __name__ == "__main__":
    import sys
    import MySQLdb

    #declaring some variable and initialise them with the arguments
    username = sys.argv[1]
    passw = sys.argv[2]
    ourdb = sys.argv[3]
    my_host = 'localhost'
    port = 3306

    #establishing the connection
    ourdb = MySQLdb.connect(
        host=my_host, user=username, passwd=passw, db=ourdb, port=port
        )

    #creating cursor
    corse = ourdb.cursor()

    #executing the query
    corse.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    
    # retriving the answer printing the result
    result = corse.fetchall()
    for city in result:
        print(city)

    #closing corsor And the connection object
    corse.close()
    ourdb.close()
