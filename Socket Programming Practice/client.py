import socket

if __name__ == "__main__":
    HOST = "127.0.0.1"
    PORT = 9090

    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.connect((HOST, PORT))
    socket.send("Jai Shree Ram!!".encode("UTF-8"))
    
    