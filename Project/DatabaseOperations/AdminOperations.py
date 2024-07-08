from .DatabaseConnection import DatabaseConnection
from DatabaseOperations.UserOperations import UserOperations

class AdminOperations:
    def __init__(self) -> None:
        self.databaseConnection = DatabaseConnection()

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
    
    def createNotification(self, message):
        connection = self.databaseConnection.makeConnection()
        cursor = connection.cursor()

        # fetching all users from user table
        userOperations = UserOperations()
        allUsersList = userOperations.selectAllUsers()

        # print(allUsersList)

        # creating the notification for each employee
        sql = "INSERT INTO notification (message, userName, isSeen) VALUES (%s, %s, %s)"
        values = None
        for user in allUsersList:
            values = (message, user[0], 0)
            cursor.execute(sql, values)
            connection.commit()
            # print(values)
            # print("Notification is created.")
        

        cursor.close()
        self.databaseConnection.closeConnection()
