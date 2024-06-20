from .User import User
from DatabaseOperations.MySQLOperations import MySQLOperations
from ProtocolDataUnit import ProtocolDataUnit

class Admin(User):
    def __init__(self, userName, password, role = 'Admin') -> None:
        super().__init__(userName, password, role)


    def startPoint(self):
        print("Welcome to Admin Portal!")
        self.login()

    def mainMenu(self):
        print("1 for add meal, 2 for remove meal, 3 for update price, 4 for updateAvailability, and 5 for logout: ")
        adminChoice = int(input())
        
        if adminChoice == 1:
            itemID = input("Enter itemID: ")
            itemName = input("Enter itemName: ")
            price = int(input("Enter price: "))
            availability = int(input("Enter availability: "))
            values = (itemID, itemName, price, availability)
            self.addMeal(values)
        if adminChoice == 2:
            itemID = input("Enter itemID: ")
            self.removeMeal(itemID)
        if adminChoice == 3:
            itemID = input("Enter itemID: ")
            newPrice = int(input("Enter new price: "))
            values = (itemID, newPrice)
            self.updatePrice(values)
        if adminChoice == 4:
            itemID = input("Enter itemID: ")
            newAvailability = int(input("Enter new price: "))
            values = itemID, newAvailability
            self.updateAvailability(values)
        if adminChoice == 4:
            self.logout()

    

    def addMeal(self, values):
        if self.loggedIn == True:
            MySQLOperations().insertFoodItem(values)

    def removeMeal(self, itemId):
        if self.loggedIn == True:
            MySQLOperations().removeFoodItem(itemId)

    def updatePrice(self, itemId, newPrice):
        if self.loggedIn == True:
            MySQLOperations.updatePrice(itemId, newPrice)

    def updateAvailability(self, itemId, newAvailability):
        if self.loggedIn == True:
            MySQLOperations.updateAvailability(itemId, newAvailability)


    

if __name__ == "__main__":
    obj = Admin('Manish', 'ps', 'Data Engineer')
    obj.addMeal(('#3', 'sabji', 200, True))
    # obj.removeMeal('#2')