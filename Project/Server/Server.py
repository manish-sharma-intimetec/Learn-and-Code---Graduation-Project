import threading
import socket

class Server:
    def __init__(self, HOST: str, PORT: int) -> None:
        self.HOST = HOST
        self.PORT = PORT
    
    def createSocket(self, HOST: str, PORT: int) -> socket.socket:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((HOST, PORT))
        return server
    
    def listenClient(self, server: socket.socket):
        connection, clientAddress = server.accept()  
        # print(connection)
        data = connection.recv(1024).decode("UTF-8")
        print(data)
    
    def listenMultipleClients(self):
        server = self.createSocket(self.HOST, self.PORT)
        server.listen()
        
        while True:
            thread = threading.Thread(target=self.listenClient, args=(server,))
            thread.start()


if __name__ == "__main__":
    print(type(socket.socket(socket.AF_INET, socket.SOCK_STREAM)))
    server = Server("127.0.0.1", 5000)
    server.listenMultipleClients()

