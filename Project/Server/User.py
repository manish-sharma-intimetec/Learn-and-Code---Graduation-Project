import socket
import sys
sys.path.append("..")
from ProtocolDataUnit import ProtocolDataUnit

# added_path = os.path.abspath("..")
# print(f"Added Path: {added_path}")
from DatabaseOperations.UserOperations import UserOperations

class User:
    def __init__(self, userName, password, role) -> None:
        self.userName = userName
        self.password = password
        self.role = role
        self.loggedIn = False

    def login(self) -> bool:
        userOperations = UserOperations()
        result = userOperations.selectUser(self.userName, self.password)

        if result[0][0] == self.userName and result[0][1] == self.password and result[0][2] == self.role:
            self.loggedIn = True
            return True



    

if __name__ == "__main__":
    HOST = "127.0.0.1"
    PORT = 5000

    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.connect((HOST, PORT))
    obj = User('Manish', '123', 'Big Data Engineer')
    obj.login(soc)
    # obj.logout(soc)
