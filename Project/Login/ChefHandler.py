import sys
sys.path.append("..")
from DatabaseOperations.AdminOperations import AdminOperations
from RecommendationEngine.RecommendationEngine import RecommendationEngine


class ChefHandler:
    def __init__(self, listOfUsersLoggedIn) -> None:
        self.listOfUsersLoggedIn = listOfUsersLoggedIn


    def getRecommendedMenu():
        try:
            recommendedItems = RecommendationEngine.getTopItems(2)
        except Exception:
            print("Error in Recommendation Engine.")
        
        return recommendedItems

    def broadcastMenu(self, lund):

        print("broadcasting......")
        finalMenu = None
        try:
            finalMenu = self.getRecommendedMenu()  
        except Exception:
            print("Something went wrong in recommendation engine")
        print(finalMenu)

        for key in self.listOfUsersLoggedIn:
            user = self.listOfUsersLoggedIn[key]
            if user.role == 'Employee':
                key.sendall(f"{finalMenu}".encode("UTF-8"))
