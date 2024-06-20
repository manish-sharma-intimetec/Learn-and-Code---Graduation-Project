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
            self.addMeal()
        if adminChoice == 2:
            self.removeMeal()
        if adminChoice == 3:
            self.updatePrice()
        if adminChoice == 4:
            self.updateAvailability()
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
    obj.removeMeal('#2')