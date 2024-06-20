import socket
import sys
sys.path.append("..")
from ProtocolDataUnit import ProtocolDataUnit

# added_path = os.path.abspath("..")
# print(f"Added Path: {added_path}")


from DatabaseOperations.MySQLOperations import MySQLOperations
class User:
    def __init__(self, userName, password, role) -> None:
        self.userName = userName
        self.password = password
        self.role = role
        self.loggedIn = False

    def login(self, connection) -> bool:

        pdu = ProtocolDataUnit()
        pdu.PDU['requestType'] = 'login'
        pdu.PDU['payload'] = (self.userName, self.password, self.role)


        connection.sendall(f"{pdu.PDU}".encode("UTF-8"))

        self.loggedIn = True
        

        
        # result = MySQLOperations().selectUser(self.userName, self.password)
        # print(result)
        
        # if(len(result) == 1 and result[0][0] == self.userName and result[0][1] == self.password and result[0][2] == self.role):
        #     print('User Authenticated.')
        #     self.loggedIn = True
        #     MySQLOperations().updateLoginStatus((self.userName, True))
        # else:
        #     print('Incorrect Credentials.')
        
        # return self.loggedIn

    def logout(self, connection):
        pdu = ProtocolDataUnit()
        pdu.PDU['requestType'] = 'logout'
        pdu.PDU['payload'] = (self.userName, self.password, self.role)

        connection.sendall(f"{pdu.PDU}".encode("UTF-8"))
        # if connection.recv(1024000).decode("UTF-8") == 'True':
        #     self.loggedIn = True
        # print(connection.recv(1024000).decode("UTF-8"))
    
    def isUserLoggedIn(self):
        result = MySQLOperations().selectUserFromLoginStatus((self.userName, ))
        if result[0][1] == True:
            return True

    

if __name__ == "__main__":
    HOST = "127.0.0.1"
    PORT = 5000

    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.connect((HOST, PORT))
    obj = User('Manish', '123', 'Big Data Engineer')
    obj.login(soc)
    # obj.logout(soc)
