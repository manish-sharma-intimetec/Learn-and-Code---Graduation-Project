from DatabaseConnection import DatabaseConnection

class MySQLOperations:
    def __init__(self) -> None:
        self.databaseConnection = DatabaseConnection()

    def insertUser(self, values = ('Manish', '123', 'Big Data Engineer')):
        connection = self.databaseConnection.makeConnection()
        cursor = connection.cursor()

        sql = "INSERT INTO users (userName, password, role) VALUES (%s, %s, %s)"
        cursor.execute(sql, values)
        connection.commit()
        print("Record inserted successfully in users table.")

        cursor.close()
        self.databaseConnection.closeConnection()


if __name__ == "__main__":
    MySQLOperations().insertUser()


