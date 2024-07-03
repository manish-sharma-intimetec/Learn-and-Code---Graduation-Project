# import sys
# sys.path.append("..")
# from Login.ChefHandler import ChefHandler

from ProtocolDataUnit import ProtocolDataUnit

class ChefMenu:
    def __init__(self, connection, userName, password, role = "Chef") -> None:
        self.connection = connection
        self.userName = userName
        self.password = password
        self.role = role

    
    def showOptions(self):
        print("Enter 1 to broadcast Recommended Items: ")
        print("Enter 2 for see voting: ")
        print("Enter 3 for today Menu: ")
        print("Enter 4 for show menu: ")


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

    
    def callService(self, choice):
        if choice == 1:
            self.broadcastMenu()
        if choice == 2:
            self.showVotingResult()
        if choice == 3:
            self.todayMeal()
        # if choice == 4:
        #     self.updatePrice()
        # if choice == 5:
        #     self.updateAvailability()