import threading
import socket
from ProtocolDataUnit import ProtocolDataUnit
import sys
sys.path.append("..")
from Login.Admin import Admin
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
    

    def loginRequest(self, PDU):
        user = None
        print('loginRequest is called.')
        print(PDU['payload'])
        if PDU['userType'] == 1:
            user = Admin(PDU['payload'][0], PDU['payload'][1])
            user.login()

    def processRequest(self, PDU):
        print("processRequest is called.")
        if PDU['loginRequest'] == True:
            self.loginRequest(PDU)
            


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
        data = connection.recv(1024).decode("UTF-8")
        # print(data)
        PDU = self.convertProtocolDataUnitIntoDictionary(data)
        print(PDU)

        # self.sendResponse(connection, PDU, "Got your Request.")
        self.processRequest(PDU)
        # self.sendResponse(connection, PDU, "Got your Request.")
        # connection.send("Hello".encode('utf-8'))
        return data
    
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

