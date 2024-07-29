# import sys
# sys.path.append("..")
# from Login.ChefHandler import ChefHandler
import json

from ProtocolDataUnit import ProtocolDataUnit

class ChefMenu:
    def __init__(self, connection, userName, password, role = "Chef") -> None:
        self.connection = connection
        self.userName = userName
        self.password = password
        self.role = role

    
    def showOptions(self):
        print("Enter 1 to see Recommended Items: ")
        print("Enter 2 for see voting: ")
        print("Enter 3 for today Menu: ")
        print("Enter 4 for show menu: ")
        print("Enter 5 for discard menu list: ")


        chefChoice = int(input())
        return chefChoice
    
    def broadcastMenu(self):
        pdu = ProtocolDataUnit()
        pdu.PDU["userName"] = self.userName
        pdu.PDU["userPassword"] = self.password
        pdu.PDU["userRole"] = self.role
        pdu.PDU["requestedFor"] = "broadcastMenu"

        self.connection.sendall(f"{pdu.PDU}".encode("UTF-8"))
        message = self.connection.recv(1024).decode("UTF-8")
        print(message)



    def showVotingResult(self):
        pdu = ProtocolDataUnit()
        pdu.PDU["userName"] = self.userName
        pdu.PDU["userPassword"] = self.password
        pdu.PDU["userRole"] = self.role
        pdu.PDU["requestedFor"] = "showVotingResult"

        self.connection.sendall(f"{pdu.PDU}".encode("UTF-8"))
        message = self.connection.recv(1024).decode("UTF-8")
        print(message)

    
    def todayMeal(self):
        pdu = ProtocolDataUnit()

        pdu.PDU["userName"] = self.userName
        pdu.PDU["userPassword"] = self.password
        pdu.PDU["userRole"] = self.role
        pdu.PDU["requestedFor"] = "showVotingResult"
        self.connection.sendall(f"{pdu.PDU}".encode("UTF-8"))
        message = self.connection.recv(1024).decode("UTF-8")
        print(message)

        while True:
            itemID = input("Enter item id to add or press 0 to submit: ")
            if itemID == '0':
                break
            
            pdu.PDU["userName"] = self.userName
            pdu.PDU["userPassword"] = self.password
            pdu.PDU["userRole"] = self.role
            pdu.PDU["itemID"] = itemID
            pdu.PDU["requestedFor"] = "todayMeal"
        

            self.connection.sendall(f"{pdu.PDU}".encode("UTF-8"))
            message = self.connection.recv(1024).decode("UTF-8")
            print(message)


    def discardItem(self, itemID = None):
        itemID = input("Enter item id to discard: ")
        payloadDict = {"itemID": itemID}
        payload = json.dumps(payloadDict)

        pdu = ProtocolDataUnit()
        pdu.PDU["userName"] = self.userName
        pdu.PDU["userPassword"] = self.password
        pdu.PDU["userRole"] = self.role
        pdu.PDU["requestedFor"] = "discardItem"
        pdu.PDU["payload"] = payload

        self.connection.sendall(f"{pdu.PDU}".encode("UTF-8"))
        message = self.connection.recv(1024).decode("UTF-8")
        print(message)


    def rollOutQuestionsForDiscardedItems(self):
        pdu = ProtocolDataUnit()

        pdu.PDU["userName"] = self.userName
        pdu.PDU["userPassword"] = self.password
        pdu.PDU["userRole"] = self.role
        pdu.PDU["requestedFor"] = "rollOutQuestionsForDiscardedItems"
        self.connection.sendall(f"{pdu.PDU}".encode("UTF-8"))
        message = self.connection.recv(1024).decode("UTF-8")
        print(message)

    def discardMenuService(self):
        self.showDiscardMenu()

        choice = int(input("Enter 1 to discard item and 2 for roll out questions: "))
        if choice == 1:
            self.discardItem()
        elif choice == 2:
            self.rollOutQuestionsForDiscardedItems()
    
    def showDiscardMenu(self):
        pdu = ProtocolDataUnit()

        pdu.PDU["userName"] = self.userName
        pdu.PDU["userPassword"] = self.password
        pdu.PDU["userRole"] = self.role
        pdu.PDU["requestedFor"] = "showDiscardMenu"
        self.connection.sendall(f"{pdu.PDU}".encode("UTF-8"))
        message = self.connection.recv(1024).decode("UTF-8")
        print(message)

    
    

    def callService(self, choice):
        if choice == 1:
            self.broadcastMenu()
        if choice == 2:
            self.showVotingResult()
        if choice == 3:
            self.todayMeal()
        # if choice == 4:
        #     self.updatePrice()
        if choice == 5:
            self.discardMenuService()