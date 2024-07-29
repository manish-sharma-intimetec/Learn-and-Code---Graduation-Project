import sys
sys.path.append("..")

import threading
import socket
import ast
from ProtocolDataUnit import ProtocolDataUnit
from Login.User import User
from DatabaseOperations.AdminOperations import AdminOperations
from Login.ChefHandler import ChefHandler
from DatabaseOperations.EmployeeOperations import EmployeeOperations



class Server:
    def __init__(self, HOST: str, PORT: int) -> None:
        self.HOST = HOST
        self.PORT = PORT
        self.listOfUsersLoggedIn = {} 

    def createSocket(self, HOST: str, PORT: int) -> socket.socket:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((HOST, PORT))
        return server
        
    def convertReceivedDataIntoDictionary(self, data: str) -> dict:
        data = ast.literal_eval(data)
        return data
    

    def processRequest(self, connection, receivedDataDict):
        print("Processing Request....")
        user = User(receivedDataDict["userName"], receivedDataDict["userPassword"], receivedDataDict["userRole"])

        if(receivedDataDict["requestedFor"] == "login"):
            if user.login() == True:

                #adding the user with key value pair if he/she successfully loggedIn
                self.listOfUsersLoggedIn[connection] = user
                print("User login successfully.")
                connection.sendall("True".encode("UTF-8"))
            else:
                print("Incorrect credentials.")
                connection.sendall("False".encode("UTF-8"))

        if(receivedDataDict["requestedFor"] == "logout"):
            self.listOfUsersLoggedIn.pop(connection)
            connection.sendall("You logout successfully.".encode("UTF-8"))
            connection.close()

        # Admin Requests
        if(receivedDataDict["requestedFor"] == "showAllItems"):
            adminOperations = AdminOperations()
            result = adminOperations.showAllItems()
            connection.send(f"{result}".encode("UTF-8"))


        if(receivedDataDict["requestedFor"] == "insertFoodItem"):
            payload = receivedDataDict["payload"]
            payloadDict = self.convertReceivedDataIntoDictionary(payload)
            

            itemID = payloadDict["itemID"]
            itemName = payloadDict["itemName"]
            price = payloadDict["price"]
            availability = payloadDict["availability"]
            foodPreference = payloadDict["foodPreference"]
            spiceLevel = payloadDict["spiceLevel"]
            vegType = payloadDict["foodType"]
            isSweet = payloadDict["sweetPreference"]

            adminOperations = AdminOperations()
            adminOperations.insertFoodItem((itemID, itemName, price, availability, foodPreference, spiceLevel, vegType, isSweet))
            connection.send(f"Item inserted successfully.".encode("UTF-8"))

            adminOperations.createNotification(f"New Item is added to Menu. Item Name: {itemName}, Price: {price}")

        if(receivedDataDict["requestedFor"] == "removeFoodItem"):
            payload = receivedDataDict["payload"]
            payloadDict = self.convertReceivedDataIntoDictionary(payload)
            itemID = payloadDict["itemID"]

            adminOperations = AdminOperations()
            adminOperations.removeFoodItem(itemID)
            connection.send(f"Item for itemID = {itemID} is removed successfully.".encode("UTF-8"))

            adminOperations.createNotification(f"Item is removed to Menu. Item Name: {itemID}")

        if(receivedDataDict["requestedFor"] == "updatePrice"):
            payload = receivedDataDict["payload"]
            payloadDict = self.convertReceivedDataIntoDictionary(payload)
            itemID = payloadDict["itemID"]
            price = payloadDict["price"]

            adminOperations = AdminOperations()
            adminOperations.updatePrice(itemID, price)
            connection.send(f"Price is updated for {itemID} successfully.".encode("UTF-8"))

            adminOperations.createNotification(f"Price is updated for an item. Item Name: {itemName}, Price: {price}")
        
        if(receivedDataDict["requestedFor"] == "updateAvailability"):
            payload = receivedDataDict["payload"]
            payloadDict = self.convertReceivedDataIntoDictionary(payload)
            itemID = payloadDict["itemID"]
            availability = payloadDict["availability"]

            adminOperations.createNotification(f"Item is availability is updated. Item Name: {itemName}, Availability: {availability}")



            adminOperations = AdminOperations()
            adminOperations.updateAvailability(itemID, availability)
            connection.send(f"Availability is updated for {itemID} successfully.".encode("UTF-8"))    

        


        # chef features
        if receivedDataDict["requestedFor"] == "broadcastMenu":
            chefHandler = ChefHandler(connection, self.listOfUsersLoggedIn)
            chefHandler.broadcastMenu(2)

        if receivedDataDict["requestedFor"] == "showVotingResult":
            chefHandler = ChefHandler(connection, self.listOfUsersLoggedIn)
            chefHandler.showVotingResult()

        if receivedDataDict["requestedFor"] == "todayMeal":
            itemID = receivedDataDict["itemID"]
            
            chefHandler = ChefHandler(connection, self.listOfUsersLoggedIn)
            chefHandler.todayMeal(itemID)
        
        if receivedDataDict["requestedFor"] == "showDiscardMenu":
            chefHandler = ChefHandler(connection, self.listOfUsersLoggedIn)
            chefHandler.showDiscardMenu()

        if receivedDataDict["requestedFor"] == "rollOutQuestionsForDiscardedItems":
            chefHandler = ChefHandler(connection, self.listOfUsersLoggedIn)
            chefHandler.rollOutQuestionsForDiscardedItems()

        if receivedDataDict["requestedFor"] == "discardItem":
            payload = receivedDataDict["payload"]
            payloadDict = self.convertReceivedDataIntoDictionary(payload)
            itemID = payloadDict["itemID"]

            chefHandler = ChefHandler(connection, self.listOfUsersLoggedIn)
            chefHandler.discardItem(itemID)

        # Employee features
        if receivedDataDict["requestedFor"] == "addVote":
            payload = receivedDataDict["payload"]
            payloadDict = self.convertReceivedDataIntoDictionary(payload)

            userName = receivedDataDict["userName"]
            itemID = payloadDict["itemID"]

            try:
                EmployeeOperations().addVote(userName, itemID)
            except Exception:
                print("Error in insertion of vote.")

            connection.send(f"Vote is added for {itemID} successfully.".encode("UTF-8"))

        if receivedDataDict["requestedFor"] == "addFeedback":
            payload = receivedDataDict["payload"]
            payloadDict = self.convertReceivedDataIntoDictionary(payload)

            userName = receivedDataDict["userName"]
            itemID = payloadDict["itemID"]
            rating = payloadDict["rating"]
            comment = payloadDict["comment"]

            # print(userName)
            # print(comment)
    

            try:
                EmployeeOperations().addFeedback(itemID, userName, rating, comment)
            except Exception:
                print("Insertion failed in feedback.")
            
            connection.send(f"Feedback is added for {itemID} successfully.".encode("UTF-8"))
        

        if receivedDataDict["requestedFor"] == "seeTodayMeal":
            result = EmployeeOperations().seeTodayMeal()
            connection.send(f"{result}".encode("UTF-8"))

        if receivedDataDict["requestedFor"] == "seeNotification":
            userName = receivedDataDict['userName']
            result = EmployeeOperations().seeNotification(userName)
            connection.send(f"{result}".encode("UTF-8"))

        if receivedDataDict["requestedFor"] == "updateProfile":
            userName = receivedDataDict['userName']
            payload = receivedDataDict["payload"]
            payloadDict = self.convertReceivedDataIntoDictionary(payload)

            foodType = payloadDict['foodType']
            spiceLevel = payloadDict['spiceLevel']
            foodPreference = payloadDict['foodPreference']
            sweetPreference = payloadDict['sweetPreference']

            try:
                EmployeeOperations().updateProfile(userName, foodType, spiceLevel, foodPreference, sweetPreference)
                connection.send(f"profile updated successfully.".encode("UTF-8"))
            except Exception:
                print("Some exception occured.")

    def listenClient(self, connection) -> str:   
        try:
            while True:
                data = connection.recv(1024).decode("UTF-8")
                print(f" Raw Data: {data}")
                if not data:
                    break
                
                dataDict = self.convertReceivedDataIntoDictionary(data)
                self.processRequest(connection, dataDict)

        except Exception:
            print("Connection is lost.")

        finally:
            self.listOfUsersLoggedIn.pop(connection, "User is already logout.") # logout
            print("User is logout due to connection lost.")
            print("Connection is closed.")
            connection.close()

    def listenMultipleClients(self):
        server = self.createSocket(self.HOST, self.PORT)
        server.listen()
        
        while True:
            connection, clientAddress = server.accept()
            thread = threading.Thread(target=self.listenClient, args=(connection, ))
            thread.start()


if __name__ == "__main__":
    print("Listening....")
    server = Server("localhost", 5000)
    server.listenMultipleClients()