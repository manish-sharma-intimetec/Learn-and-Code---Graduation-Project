import socket
import time
from ProtocolDataUnit import ProtocolDataUnit

import sys
sys.path.append("..")
from Login.Admin import Admin
from Login.Chef import Chef




def getUserType():
    userType = int(input("Enter 1 for Admin, 2 for Chef, and 3 for Employee: "))
    return userType

def askForUserCredentials():
    userName = input("Enter your userName: ")
    password = input("Enter your password: ")
    return (userName, password)

def createUserObject(userType, credentials):
    user = None
    if userType == 1:
        user = Admin(credentials[0], credentials[1], 'Admin')
    elif userType == 2:
        user = Chef(credentials[0], credentials[1], 'Chef')
    elif userType == 3:
        pass

    return user

# def logoutUser(user):
#     user.logout()

if __name__ == "__main__":
    HOST = "127.0.0.1"
    PORT = 5000

    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.connect((HOST, PORT))

    userType = getUserType()
    credentials = askForUserCredentials()
    user = createUserObject(userType, credentials)
    user.login(soc)
    
    

    if user.isUserLoggedIn():
        user.mainMenu()

    # user.mainMenu()
    

    # pdu = ProtocolDataUnit()
    # pdu.PDU['payload'] = credentials
    # pdu.PDU['status'] = 'OK'
    # pdu.PDU['userType'] = 1
    # pdu.PDU['requestType'] = 'login'
    # pdu.PDU['time'] =  time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


        # login
    # soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # soc.connect((HOST, PORT))
        # soc.sendall(f"{pdu.PDU}".encode("UTF-8"))
        # print(soc.recv(10240000).decode('utf-8'))
        # soc.close()


    #logout

    # int(input("Enter to logout."))
    # pdu.PDU['payload'] = credentials
    # pdu.PDU['status'] = 'OK'
    # pdu.PDU['userType'] = 1
    # pdu.PDU['requestType'] = 'logout'
    # pdu.PDU['time'] =  time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    # soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # soc.connect((HOST, PORT))
    
    # while True:
    #     pass


    # for i in range(10):
    #     soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #     soc.connect((HOST, PORT))
    #     soc.send(f"client: {i + 1}".encode("UTF-8"))
    #     time.sleep(1.5)




    # userType = getUserType()
    # credentials = askForUserCredentials()
    # createUserAccordingToUserType(userType, credentials)



    