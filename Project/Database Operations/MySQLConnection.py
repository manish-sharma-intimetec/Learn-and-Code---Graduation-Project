import mysql.connector
from DatabaseConfig import config

class MySQLConnection:
    def __init__(self) -> None:
        self.connection = None

    def makeConnection(self) -> mysql.connector.MySQLConnection:
        try:
            self.connection = mysql.connector.connect(**config)
            if self.connection != None and self.connection.is_connected() == True:
                print("Connection to MySQL is created successfully.")        
        except Exception:
            print(f"Some Exception occured while connecting to MySQL and the exception is : {Exception}")
        return self.connection
    
    def closeConnection(self):
        if self.connection != None and self.connection.is_connected() == True:
            self.connection.close()
            print(f"Connection with MySQL is closed.")
        else:
            print("There is no connection with MySQL.")


mysqlConnection = MySQLConnection()
mysqlConnection.makeConnection()
mysqlConnection.closeConnection()