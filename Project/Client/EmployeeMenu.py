# import sys
# sys.path.append("..")
# from Login.ChefHandler import ChefHandler
import json

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


        chefChoice = int(input())
        return chefChoice
    
    def callService(self, choice):
        if choice == 1:
            self.addVote()
        if choice == 2:
            self.addFeedback()
    
    def addFeedback(self, itemID = None, rating = 0, comment = "no comment"):
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

        self.connection.sendall(f"{pdu.PDU}".encode("UTF-8"))
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
    
    
      