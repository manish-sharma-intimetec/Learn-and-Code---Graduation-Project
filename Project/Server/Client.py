import socket
import time
from ProtocolDataUnit import ProtocolDataUnit

if __name__ == "__main__":
    HOST = "127.0.0.1"
    PORT = 5000

    pdu = ProtocolDataUnit()
    pdu.PDU['payload'] = "Hello Moto!"
    pdu.PDU['status'] = 'OK'
    pdu.PDU['time'] =  time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.connect((HOST, PORT))
    soc.send(f"{pdu.PDU}".encode("UTF-8"))
    print(soc.recv(1024).decode('utf-8'))
    
    # for i in range(10):
    #     soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #     soc.connect((HOST, PORT))
    #     soc.send(f"client: {i + 1}".encode("UTF-8"))
    #     time.sleep(1.5)
    
    