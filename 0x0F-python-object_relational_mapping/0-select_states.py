#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

def list_states(username, password, database_name):
    # Establish a connection to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database_name)

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute the SELECT query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows returned by the query
    rows = cursor.fetchall()

    # Iterate over the rows and print each state
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()

# Call the list_states function with the provided arguments
list_states(sys.argv[1], sys.argv[2], sys.argv[3])
