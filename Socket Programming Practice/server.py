import socket

def createSocket(host, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))

    return server


def printClientData(connectionSocket):
    data = connectionSocket.recv(1024).decode("UTF-8")
    print(data)
    return


def acceptConnectionRequests(server):
    while True:
        connectionSocket, clientAddress = server.accept()
        printClientData(connectionSocket)


if __name__ == "__main__":
    HOST = "127.0.0.1"
    PORT = 9090
    server = createSocket(HOST, PORT)
    server.listen()
    acceptConnectionRequests(server)

    