import socket
import time
from CustomProtocol import *

if __name__ == "__main__":
    HOST = "127.0.0.1"
    PORT = 5000

    for i in range(10):
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc.connect((HOST, PORT))
        soc.send(f"client: {i + 1}".encode("UTF-8"))
        time.sleep(1.5)
    
    