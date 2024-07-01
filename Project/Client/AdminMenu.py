from ProtocolDataUnit import ProtocolDataUnit
import json

class AdminMenu:
    def __init__(self, connection, name, password, role = "Admin") -> None:
        self.connection = connection
        self.name = name
        self.password = password
        self.role = role

    def showOptions(self):
        print("Enter 1 to add a item: ")
        print("Enter 2 to remove a item: ")
        print("Enter 3 to update the price: ")
        print("Enter 4 to update availability: ")

        adminChoice = int(input())
        return adminChoice

    def addItem(self, itemID, itemName, price, availability = 1):
        
        payloadDict = {"itemID": itemID, 
               "itemName": itemName,
               "price": price,
               "availability": availability}
        
        payload = json.dumps(payloadDict)
        
        pdu = ProtocolDataUnit()
        pdu.PDU["userName"] = self.name
        pdu.PDU["userPassword"] = self.password
        pdu.PDU["userRole"] = self.role
        pdu.PDU["requestedFor"] = "insertFoodItem"
        pdu.PDU["Payload"] = payload

        self.connection.sendall(f"{pdu.PDU}".encode("UTF-8"))
        
        message = self.connection.recv(1024).decode("UTF-8")
        print(message)

    
