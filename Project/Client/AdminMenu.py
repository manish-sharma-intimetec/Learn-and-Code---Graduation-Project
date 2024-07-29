from ProtocolDataUnit import ProtocolDataUnit
import json

class AdminMenu:
    def __init__(self, connection, name, password, role = "Admin") -> None:
        self.connection = connection
        self.name = name
        self.password = password
        self.role = role

    def showOptions(self):
        print("Enter 1 to show menu: ")
        print("Enter 2 to insert a item: ")
        print("Enter 3 to remove a item: ")
        print("Enter 4 to update the price: ")
        print("Enter 5 to update availability: ")

        adminChoice = int(input())
        return adminChoice
    
    def callService(self, choice):
        if choice == 1:
            self.showAllItems()
        if choice == 2:
            self.addItem()
        if choice == 3:
            self.removeItem()
        if choice == 4:
            self.updatePrice()
        if choice == 5:
            self.updateAvailability()

    def showAllItems(self):
        pdu = ProtocolDataUnit()
        pdu.PDU["userName"] = self.name
        pdu.PDU["userPassword"] = self.password
        pdu.PDU["userRole"] = self.role
        pdu.PDU["requestedFor"] = "showAllItems"

        self.connection.sendall(f"{pdu.PDU}".encode("UTF-8"))
        message = self.connection.recv(1024).decode("UTF-8")
        print(message)

    def addItem(self, itemID = None, itemName = None, price = None, availability = 1):
        
        itemID = input("Enter item id: ")
        itemName = input("Enter item name: ")
        price = int(input("Enter price: "))
        availability = int(input("Enter availability: "))
        foodType = input("Enter what do like Veg /Non Veg/ Eggetarian: ")
        spiceLevel = input("Enter Spice Level - Low / Medium / High: ")
        foodPreference = input("Enter food preference - North Indian / South Indian: ")
        sweetPreference = input("Enter sweet preference - Yes / No: ")


        payloadDict = {"itemID": itemID, 
               "itemName": itemName,
               "price": price,
               "availability": availability,
               "foodType": foodType,
                "spiceLevel": spiceLevel,
                "foodPreference": foodPreference,
                "sweetPreference": sweetPreference
               }
        
        payload = json.dumps(payloadDict)
        
        pdu = ProtocolDataUnit()
        pdu.PDU["userName"] = self.name
        pdu.PDU["userPassword"] = self.password
        pdu.PDU["userRole"] = self.role
        pdu.PDU["requestedFor"] = "insertFoodItem"
        pdu.PDU["payload"] = payload

        self.connection.sendall(f"{pdu.PDU}".encode("UTF-8"))
        
        message = self.connection.recv(1024).decode("UTF-8")
        print(message)

    
    def removeItem(self, itemID = None):
        itemID = input("Enter item id: ")
    
        payloadDict = {"itemID": itemID}
        
        payload = json.dumps(payloadDict)
        
        pdu = ProtocolDataUnit()
        pdu.PDU["userName"] = self.name
        pdu.PDU["userPassword"] = self.password
        pdu.PDU["userRole"] = self.role
        pdu.PDU["requestedFor"] = "removeFoodItem"
        pdu.PDU["payload"] = payload

        self.connection.sendall(f"{pdu.PDU}".encode("UTF-8"))
        message = self.connection.recv(1024).decode("UTF-8")
        print(message)

    def updatePrice(self, itemID = None, price = None):
        itemID = input("Enter item id: ")
        price = int(input("Enter price: "))


        payloadDict = {"itemID": itemID, 
               "price": price
               }
        
        payload = json.dumps(payloadDict)
        
        pdu = ProtocolDataUnit()
        pdu.PDU["userName"] = self.name
        pdu.PDU["userPassword"] = self.password
        pdu.PDU["userRole"] = self.role
        pdu.PDU["requestedFor"] = "updatePrice"
        pdu.PDU["payload"] = payload

        self.connection.sendall(f"{pdu.PDU}".encode("UTF-8"))
        
        message = self.connection.recv(1024).decode("UTF-8")
        print(message)

    def updateAvailability(self):
        itemID = input("Enter item id: ")
        availability = int(input("Enter availability: "))


        payloadDict = {"itemID": itemID, 
               "availability": availability
               }
        
        payload = json.dumps(payloadDict)
        
        pdu = ProtocolDataUnit()
        pdu.PDU["userName"] = self.name
        pdu.PDU["userPassword"] = self.password
        pdu.PDU["userRole"] = self.role
        pdu.PDU["requestedFor"] = "updateAvailability"
        pdu.PDU["payload"] = payload

        self.connection.sendall(f"{pdu.PDU}".encode("UTF-8"))
        
        message = self.connection.recv(1024).decode("UTF-8")
        print(message)