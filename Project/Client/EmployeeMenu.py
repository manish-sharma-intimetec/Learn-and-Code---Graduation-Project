# import sys
# sys.path.append("..")
# from Login.ChefHandler import ChefHandler
import ast
import json
from PrintTable import *

from ProtocolDataUnit import ProtocolDataUnit

class EmployeeMenu:
    def __init__(self, connection, userName, password, role = "Employee") -> None:
        self.connection = connection
        self.userName = userName
        self.password = password
        self.role = role

    
    def showOptions(self):
        print("Enter 1 to vote: ")
        print("Enter 2 for adding feedback: ")
        print("Enter 3 for today meal: ")
        print("Enter 4 for menu items: ")
        print("Enter 5 to see notifications: ")
        print("Enter 6 to update profile: ")

        chefChoice = int(input())
        return chefChoice
    
    def callService(self, choice):
        if choice == 1:
            self.addVote()
        if choice == 2:
            self.addFeedback()
        if choice == 3:
            self.todayMeal()
        if choice == 4:
            self.showMenu()
        if choice == 5:
            self.seeNotification()
        if choice == 6:
            self.updateProfile()
    

    def seeNotification(self):
        pdu = ProtocolDataUnit()
        pdu.PDU["userName"] = self.userName
        pdu.PDU["userPassword"] = self.password
        pdu.PDU["userRole"] = self.role
        pdu.PDU["requestedFor"] = "seeNotification"

        self.connection.sendall(f"{pdu.PDU}".encode("UTF-8"))
        message = self.connection.recv(1024).decode("UTF-8")
        print(message)

    def todayMeal(self):
        pdu = ProtocolDataUnit()
        pdu.PDU["userName"] = self.userName
        pdu.PDU["userPassword"] = self.password
        pdu.PDU["userRole"] = self.role
        pdu.PDU["requestedFor"] = "seeTodayMeal"

        self.connection.sendall(f"{pdu.PDU}".encode("UTF-8"))
        message = self.connection.recv(1024).decode("UTF-8")
        print(message)
        
        message = ast.literal_eval(message)
        columnNames = ['ID', 'Item Name', 'Price', 'Availability', 'Cuisine', 'Spice Level', 'Veg Type', 'Is Sweet']
        printTable(message, columnNames)

    def showMenu(self):
        pdu = ProtocolDataUnit()
        pdu.PDU["userName"] = self.userName
        pdu.PDU["userPassword"] = self.password
        pdu.PDU["userRole"] = self.role
        pdu.PDU["requestedFor"] = "showAllItems"

        self.connection.sendall(f"{pdu.PDU}".encode("UTF-8"))
        message = self.connection.recv(1024).decode("UTF-8")
        print(message)

    def addFeedback(self, itemID = None, rating = 0, comment = "no comment"):
        
        pdu = ProtocolDataUnit()
        pdu.PDU["userName"] = self.userName
        pdu.PDU["userPassword"] = self.password
        pdu.PDU["userRole"] = self.role
        pdu.PDU["requestedFor"] = "seeTodayMeal"

        self.connection.sendall(f"{pdu.PDU}".encode("UTF-8"))
        todayMenu = self.connection.recv(1024).decode("UTF-8")
        print(todayMenu)
        
        
        itemID = input("Enter Item ID: ")
        rating = int(input("Enter rating: "))
        comment = input("Enter comment: ")


        payloadDict = {
            "itemID": itemID,
            "rating": rating,
            "comment": comment
        }
        payload = json.dumps(payloadDict)
        
        pdu = ProtocolDataUnit()
        pdu.PDU["userName"] = self.userName
        pdu.PDU["userPassword"] = self.password
        pdu.PDU["userRole"] = self.role
        pdu.PDU["requestedFor"] = "addFeedback"
        pdu.PDU["payload"] = payload

        message = self.connection.recv(1024).decode("UTF-8")
        print(message)


    def addVote(self, itemID = None):
        
        itemID = input("Enter the itemID to vote: ")
        payloadDict = {
            "itemID": itemID
        }
        payload = json.dumps(payloadDict)

        pdu = ProtocolDataUnit()
        pdu.PDU["userName"] = self.userName
        pdu.PDU["userPassword"] = self.password
        pdu.PDU["userRole"] = self.role
        pdu.PDU["requestedFor"] = "addVote"
        pdu.PDU["payload"] = payload

        self.connection.sendall(f"{pdu.PDU}".encode("UTF-8"))
        message = self.connection.recv(1024).decode("UTF-8")
        print(message)

    
    def updateProfile(self):
        foodType = input("Enter what do like Veg /Non Veg/ Eggetarian: ")
        spiceLevel = input("Enter Spice Level - Low / Medium / High: ")
        foodPreference = input("Enter food preference - North Indian / South Indian: ")
        sweetPreference = input("Enter sweet preference - Yes / No: ")
        
        payloadDict = {
            "foodType": foodType,
            "spiceLevel": spiceLevel,
            "foodPreference": foodPreference,
            "sweetPreference": sweetPreference
        }
        payload = json.dumps(payloadDict)
        
        pdu = ProtocolDataUnit()
        pdu.PDU["userName"] = self.userName
        pdu.PDU["userPassword"] = self.password
        pdu.PDU["userRole"] = self.role
        pdu.PDU["requestedFor"] = "updateProfile"
        pdu.PDU["payload"] = payload

        self.connection.sendall(f"{pdu.PDU}".encode("UTF-8"))
        message = self.connection.recv(1024).decode("UTF-8")
        print(message)
    
    
      