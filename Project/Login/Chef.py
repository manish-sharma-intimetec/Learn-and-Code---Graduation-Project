from .User import User
from ProtocolDataUnit import ProtocolDataUnit
from DatabaseOperations.MySQLOperations import MySQLOperations

class Chef(User):
    def __init__(self, userName, password, role = 'Chef') -> None:
        super().__init__(userName, password, role)

    def mainMenu(self):
        chefChoice = int(input('Enter 1 for view Menu, 2 for Recommended Items, 3 for Voting Results, roll out menu'))

        if chefChoice == 1:
            self.showMenuItem("con")

    def showMenuItem(self, connection):
        # pdu = ProtocolDataUnit()
        # pdu.PDU['requestType'] = 'showMenu'
        # pdu.PDU['userType'] = 'Chef'
        # pdu.PDU['payload'] = (self.userName, self.password, self.role)

        # send it to server

        # connection.sendall(f"{pdu.PDU}".encode("UTF-8"))
        # result = connection.recv(1024).decode('utf-8')
        # print(result)

        result = MySQLOperations().showAllItems()
        print(result)


if __name__ == "__main__":
    # Chef().showMenuItem()
    pass
