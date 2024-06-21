import threading
import socket


HOST = '127.0.0.1'
PORT = 8080

server = socket.socket(socket.AF_INET)
server.bind((HOST, PORT))
server.listen()

listOfClients = []

def broadcast(message, listOfClients):
    for client in listOfClients:
        client.send(message)


def broadcastClientMessage(client, listOfClients):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            listOfClients.remove(client)
            break


def receiveRequests():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send('Conneted to the server.'.encode('ascii'))

        thread = threading.Thread(target = broadcastClientMessage, args=(client, listOfClients))
        thread.start()


if __name__ == "__main__":
    receiveRequests()
