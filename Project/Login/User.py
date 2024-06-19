
import sys
sys.path.append("..")

# added_path = os.path.abspath("..")
# print(f"Added Path: {added_path}")


from DatabaseOperations.MySQLOperations import MySQLOperations
class User:
    def __init__(self, userName, password, role) -> None:
        self.userName = userName
        self.password = password
        self.role = role
        self.loggedIn = False

    def login(self):
        result = MySQLOperations().selectUser(self.userName, self.password)
        print(result)
        
        if(len(result) == 1 and result[0][0] == self.userName and result[0][1] == self.password and result[0][2] == self.role):
            print('User Authenticated.')
            self.loggedIn = True
        else:
            print('Incorrect Credentials.')

    def logout(self):
        pass
    


    

if __name__ == "__main__":
    User('Manish', '23', 'Junior Data Engineer').login()