from .DatabaseConnection import DatabaseConnection

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

    def selectUser(self, userName, password):
        connection = self.databaseConnection.makeConnection()
        cursor = connection.cursor()


        values = (userName, password)
        sql = "SELECT * FROM users WHERE userName = %s AND password = %s"
        
        cursor.execute(sql, values)
        result = cursor.fetchall()
        print(result)
        print("Record fetched successfully from users table.")

        cursor.close()
        self.databaseConnection.closeConnection()   
        return result

    # Menu_Item Table
    def insertFoodItem(self, values):
        connection = self.databaseConnection.makeConnection()
        cursor = connection.cursor()

        sql = "INSERT INTO Menu_Item (itemID, itemName, price, availability) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, values)
        connection.commit()
        print("Record inserted successfully in Menu_Item table.")

        cursor.close()
        self.databaseConnection.closeConnection()

    def removeFoodItem(self, itemID):
        connection = self.databaseConnection.makeConnection()
        cursor = connection.cursor()

        sql = "DELETE FROM Menu_Item WHERE itemID = %s"
        cursor.execute(sql, (itemID,))
        connection.commit()
        print("Record removed successfully from Menu_Item table.")

        cursor.close()
        self.databaseConnection.closeConnection()

          
    def updatePrice(self, itemID, newPrice):
        connection = self.databaseConnection.makeConnection()
        cursor = connection.cursor()

        sql = "UPDATE Menu_Item SET price = %s WHERE itemID = %s"
        cursor.execute(sql, (newPrice, itemID))
        connection.commit()
        print("Price updated successfully in Menu_Item table.")

        cursor.close()
        self.databaseConnection.closeConnection()

    
    def updateAvailability(self, itemID, newAvailability):
        connection = self.databaseConnection.makeConnection()
        cursor = connection.cursor()

        sql = "UPDATE Menu_Item SET availability = %s WHERE itemID = %s"
        cursor.execute(sql, (newAvailability, itemID))
        connection.commit()
        print("Availability updated successfully in Menu_Item table.")

        cursor.close()
        self.databaseConnection.closeConnection()




if __name__ == "__main__":
    # MySQLOperations().insertUser()
    # MySQLOperations().selectUser('Manish', '123')
    MySQLOperations.insertFoodItem('#1', 'Idli', 200, True)


