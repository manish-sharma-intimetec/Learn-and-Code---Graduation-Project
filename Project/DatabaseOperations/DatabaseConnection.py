from .MySQLConnection import MySQLConnection

class DatabaseConnection(MySQLConnection):
    def __init__(self) -> None:
        super().__init__()

    def makeConnection(self):
        try:
            super().makeConnection()
        except Exception:
            print(f"Some Exception occured while connecting to MySQL and the exception is : {Exception}")
        return self.connection

    def closeConnection(self):
        super().closeConnection()
    


if __name__ == "__main__":
    dbObj = DatabaseConnection()
    con = dbObj.makeConnection()
    if con.is_connected():

        dbObj.closeConnection()