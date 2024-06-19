from .User import User
from DatabaseOperations.MySQLOperations import MySQLOperations

class Admin(User):
    def __init__(self, userName, password, role = 'Admin') -> None:
        super().__init__(userName, password, role)

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