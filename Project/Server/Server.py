import threading
import socket
from ProtocolDataUnit import ProtocolDataUnit
import sys
sys.path.append("..")
from Login.Admin import Admin
from DatabaseOperations.MySQLOperations import MySQLOperations
import ast
import queue



class Server:
    def __init__(self, HOST: str, PORT: int) -> None:
        self.HOST = HOST
        self.PORT = PORT
        self.outputQueue = queue.Queue()
    
    def convertProtocolDataUnitIntoDictionary(self, data: str):
        data = ast.literal_eval(data)
        return data
    
    def isPDUValid(self, PDU: dict) -> bool:
        isValid = True

        if(PDU['status'] != 'OK'):
            isValid = False
        if(PDU['payload'] == None or len(PDU['payload']) <= 0):
            isValid = False
        if(PDU['time'] == None):
            isValid = False
        
        return isValid
    

    def loginRequest(self, connection, PDU)->bool:
        user = None
        # print('loginRequest is called.')
        print(PDU['payload'])
        userName = PDU['payload'][0]
        password = PDU['payload'][1]
        role = PDU['payload'][2]
        
        result = MySQLOperations().selectUser(userName, password)
        # print(result)
        
        if(len(result) == 1 and result[0][0] == userName and result[0][1] == password and result[0][2] == role):
            print('User Authenticated.')
            self.loggedIn = True
            MySQLOperations().updateLoginStatus((userName, True))
            connection.sendall("True".encode('UTF-8'))
        else:
            print('Incorrect Credentials.')


    #logout
    def logoutRequest(self, PDU):
        userName = PDU['payload'][0]
        MySQLOperations().updateLoginStatus((userName, False))
        print("User Logout successfully.")

    #show Menu
    def showMenu(self, connection):
        # print("called..............")
        result = MySQLOperations.showAllItems()
        connection.sendall(f"{result}".encode('UTF-8'))


    # handle request of clients
    def processRequest(self, connection, PDU):
        print("processRequest is called.")
        if PDU['requestType'] == 'login':
            self.loginRequest(connection, PDU)
        if PDU['requestType'] == 'logout':
            self.logoutRequest(PDU)
        if PDU['requestType'] == 'showMenu':
            self.showMenu(connection)
            


    def sendResponse(self, connection, clientData: dict, responseMessage: str):
        if self.isPDUValid(clientData) == True:
            connection.send(responseMessage.encode('utf-8'))
        else:
            print("PDU have some issue.")


    def createSocket(self, HOST: str, PORT: int) -> socket.socket:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((HOST, PORT))
        return server
    
    def listenClient(self, server: socket.socket) -> str:
        connection, clientAddress = server.accept()  
        
        
        try:
            while True:
                data = connection.recv(1024).decode("UTF-8")
                # print(data)
                PDU = self.convertProtocolDataUnitIntoDictionary(data)
                print(PDU)

                if not PDU:
                    break

                # connection.send("Got your request.".encode('utf-8'))
                self.processRequest(connection, PDU)

        except ConnectionResetError:
            print("Connection Lost")

        finally:
            connection.close()

    def listenMultipleClients(self):
        server = self.createSocket(self.HOST, self.PORT)
        server.listen()
        
        while True:
            thread = threading.Thread(target=self.listenClient, args=(server, ))
            thread.start()


if __name__ == "__main__":
    print(type(socket.socket(socket.AF_INET, socket.SOCK_STREAM)))
    server = Server("127.0.0.1", 5000)
    server.listenMultipleClients()

