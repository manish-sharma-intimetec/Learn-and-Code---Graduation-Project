import sys
sys.path.append("..")
from DatabaseOperations.DatabaseConnection import DatabaseConnection
from RecommendationEngine.RecommendationEngine import RecommendationEngine
from datetime import datetime


class ChefHandler:
    def __init__(self, connection, listOfUsersLoggedIn = None) -> None:
        self.connection = connection
        self.listOfUsersLoggedIn = listOfUsersLoggedIn


    


    def getRecommendedMenu(self, count = 2):
        try:
            recommendedItems = RecommendationEngine().getTopItems(count)
            # print("5")
        except Exception:
            print("Error in Recommendation Engine.")
        
        return recommendedItems

    def broadcastMenu(self, count = 2):

        print("broadcasting......")
        finalMenu = None
        try:
            finalMenu = self.getRecommendedMenu(count)  
        except Exception:
            print("Something went wrong in recommendation engine.")
        

        for key in (self.listOfUsersLoggedIn):
            user = self.listOfUsersLoggedIn[key]
            if user.role == 'Employee' or user.role == 'Chef':   
                key.sendall(f"{finalMenu}".encode("UTF-8"))


    def showVotingResult(self):
        databaseConnection = DatabaseConnection()
        dbConnection = databaseConnection.makeConnection()
        cursor = dbConnection.cursor()

        query = """
                SELECT v.itemID, mi.itemName, mi.price, COUNT(*) as vote_count
                FROM vote v
                JOIN Menu_Item mi ON v.itemID = mi.itemID
                WHERE v.date = %s
                GROUP BY v.itemID, mi.itemName, mi.price
                ORDER BY vote_count DESC;
                """
        
        currentDate = datetime.now().date()
        cursor.execute(query, (currentDate,))
        result = cursor.fetchall()
        print(result)
        
        self.connection.sendall(f"Votes: {result}".encode("UTF-8"))
        # for key in self.listOfUsersLoggedIn:
        #     user = self.listOfUsersLoggedIn[key]

        #     if user.role == "Chef":
        #         key.sendall(f"Votes: {result}".encode("UTF-8"))



    def todayMeal(self, itemID):
        databaseConnection = DatabaseConnection()
        dbConnection = databaseConnection.makeConnection()
        cursor = dbConnection.cursor()

        # votingResult = self.showVotingResult()
        # self.connection.send(f"voting Result: {votingResult}".encode("UTF-8"))

        query = "INSERT INTO todayMeal VALUES(%s, %s);"
        currentDate = datetime.now().date()
    
            
        cursor.execute(query, (itemID, currentDate))
        dbConnection.commit()

        print("Meal inserted successfully")
        self.connection.sendall(f"Meal inserted successfully".encode("UTF-8"))



if __name__ == "__main__":
    ChefHandler().todayMeal()