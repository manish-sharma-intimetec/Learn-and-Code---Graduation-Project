from .DatabaseConnection import DatabaseConnection

class MySQLOperations:
    def __init__(self) -> None:
        self.databaseConnection = DatabaseConnection()
    

    def selectUserFromLoginStatus(self, values):
        connection = self.databaseConnection.makeConnection()
        cursor = connection.cursor()

        sql = "SELECT * FROM user_status WHERE userName = %s"
        cursor.execute(sql, values)
        result = cursor.fetchall()

        cursor.close()
        self.databaseConnection.closeConnection()
        return result

    def updateLoginStatus(self, values = ('Manish', True)):
        connection = self.databaseConnection.makeConnection()
        cursor = connection.cursor()

        # delete previous entry if it is exist
        
        sql = "DELETE FROM user_status WHERE userName = %s"
        cursor.execute(sql, (values[0], ))
        print("record is updating.")

        # insert new entry
        sql = "INSERT INTO user_status (userName, loginStatus) VALUES (%s, %s)"
        cursor.execute(sql, values)
        connection.commit()
        print("Record updated successfully in user_status table.")

        cursor.close()
        self.databaseConnection.closeConnection()

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

    def showAllItems(self):
        connection = self.databaseConnection.makeConnection()
        cursor = connection.cursor()

        sql = "SELECT * FROM Menu_Item"
        cursor.execute(sql)
        result = cursor.fetchall()
        print("Fetched all records from Menu_Item.")

        cursor.close()
        self.databaseConnection.closeConnection()
        return result




if __name__ == "__main__":
    # MySQLOperations().insertUser()
    # MySQLOperations().selectUser('Manish', '123')
    # MySQLOperations.insertFoodItem('#1', 'Idli', 200, True)
    MySQLOperations().showAllItems()



