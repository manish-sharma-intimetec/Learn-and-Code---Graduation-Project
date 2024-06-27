import sys
sys.path.append("..")

import threading
import socket
import ast
from ProtocolDataUnit import ProtocolDataUnit
from Login.User import User
from DatabaseOperations.AdminOperations import AdminOperations



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
                connection.sendall("You login successfully.".encode("UTF-8"))
            else:
                print("Incorrect credentials.")

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

            adminOperations = AdminOperations()
            adminOperations.insertFoodItem((itemID, itemName, price, availability))
            connection.send(f"Item inserted successfully.".encode("UTF-8"))
            
            



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