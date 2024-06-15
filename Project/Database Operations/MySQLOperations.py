from DatabaseConnection import DatabaseConnection

class MySQLOperations:
    def __init__(self) -> None:
        self.databaseConnection = DatabaseConnection()

    def insertUser(self):
        connection = self.databaseConnection.makeConnection()
        cursor = connection.cursor()

        sql = "INSERT INTO users (userName, password, role) VALUES (%s, %s, %s)"
        values = ("Manish", "1234", "Big Data Engineer")
        cursor.execute(sql, values)
        connection.commit()
        print("Record inserted successfully in users table.")

        cursor.close()
        self.databaseConnection.closeConnection()


if __name__ == "__main__":
    MySQLOperations().insertUser()


