import os
import mysql.connector

class MySQLTestService:
    def __init__(self):
        pass

    def test(self) -> bool:
        # Connect to server
        cnx = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST"),
            port=int(os.getenv("MYSQL_PORT")),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"))

        # Get a cursor
        cur = cnx.cursor()

        # Execute a query
        cur.execute("SELECT CURDATE()")

        # Fetch one result
        row = cur.fetchone()
        print("Current date is: {0}".format(row[0]))

        # Close connection
        cnx.close()        

    def connect(self):
        # Code to establish a connection to the MySQL database
        pass

    def disconnect(self):
        # Code to close the connection to the MySQL database
        pass

    def execute_query(self, query: str):
        # Code to execute a given SQL query
        pass