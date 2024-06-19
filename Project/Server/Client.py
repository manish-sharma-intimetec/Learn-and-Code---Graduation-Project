import socket
import time
from ProtocolDataUnit import ProtocolDataUnit

import sys
sys.path.append("..")
from Login.Admin import Admin

def getUserType():
    userType = int(input("Enter 1 for Admin, 2 for Chef, and 3 for Employee: "))
    return userType

def askForUserCredentials():
    userName = input("Enter your userName: ")
    password = input("Enter your password: ")
    return (userName, password)

def createUserAccordingToUserType(userType, credentials):
    user = None
    if userType == 1:
        user = Admin(credentials[0], credentials[1], 'Admin')
    elif userType == 2:
        pass
    elif userType == 3:
        pass

    user.login()


if __name__ == "__main__":
    HOST = "127.0.0.1"
    PORT = 5000


    userType = getUserType()
    credentials = askForUserCredentials()

    pdu = ProtocolDataUnit()
    pdu.PDU['payload'] = credentials
    pdu.PDU['status'] = 'OK'
    pdu.PDU['userType'] = 1
    pdu.PDU['loginRequest'] = True
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




    # userType = getUserType()
    # credentials = askForUserCredentials()
    # createUserAccordingToUserType(userType, credentials)