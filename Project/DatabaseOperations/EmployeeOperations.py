import sys
sys.path.append("..")
from DatabaseOperations.DatabaseConnection import DatabaseConnection


class EmployeeOperations:
    def __init__(self) -> None:
        self.databaseConnection = DatabaseConnection()

    def addVote(self, userName, itemID):
        connection = self.databaseConnection.makeConnection()
        cursor = connection.cursor()

        sql = '''SELECT voteID, CAST(SUBSTRING(voteID, 2) AS UNSIGNED) AS voteIDInteger
                    FROM vote
                    ORDER BY voteIDInteger DESC
                    LIMIT 1;
                '''
        
        cursor.execute(sql)
        result = cursor.fetchall()
    
        maxVoteID = result[0][1]

        newVoteIDInteger = maxVoteID + 1
        # print(f"voteID: {newVoteIDInteger}")
        newVoteID = f"#{newVoteIDInteger}"
        
        
        insert_sql = '''INSERT INTO vote (voteID, userName, itemID, date)
                        VALUES (%s, %s, %s, CURDATE());
                    '''
        
        cursor.execute(insert_sql, (newVoteID, userName, itemID))
        connection.commit()

    
    def addFeedback(self, itemID, userName, rating, comment = None):
        connection = self.databaseConnection.makeConnection()
        cursor = connection.cursor()

        sql = '''SELECT feedbackID, CAST(SUBSTRING(feedbackID, 1) AS UNSIGNED) AS feedbackIDInteger
                FROM feedback
                ORDER BY feedbackIDInteger DESC
                LIMIT 1;'''
        
        cursor.execute(sql)
        result = cursor.fetchall()

        maxFeedbackID = result[0][1] + 1

        sql = "INSERT INTO feedback VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (maxFeedbackID, itemID, userName, rating, comment))
        connection.commit()

    def seeTodayMeal(self):
        connection = self.databaseConnection.makeConnection()
        cursor = connection.cursor()

        sql = '''
        SELECT Menu_Item.*
        FROM Menu_Item
        JOIN todayMeal ON Menu_Item.itemID = todayMeal.itemID AND todayMeal.date = CURDATE();
        '''
        
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
        return result
    
    def updateIsSeen(self, userName):
        connection = self.databaseConnection.makeConnection()
        cursor = connection.cursor()

        sql = ''' UPDATE notification
                    SET isSeen = 1
                    WHERE userName = %s;
                '''
        
        cursor.execute(sql, (userName, ))
        connection.commit()

    def seeNotification(self, userName):
        connection = self.databaseConnection.makeConnection()
        cursor = connection.cursor()

        sql = '''SELECT message FROM notification
                WHERE userName = %s AND isSeen = 0;
                '''
        
        cursor.execute(sql, (userName, ))
        result = cursor.fetchall()
        print(result)

        self.updateIsSeen(userName)
        return result
    
    def updateProfile(self, userName, foodType, spiceLevel, foodPreference, sweetPreference):
        connection = self.databaseConnection.makeConnection()
        cursor = connection.cursor()

        query = "UPDATE user_profile SET foodType = %s, spiceLevel = %s, foodPreference = %s, sweetPreference = %s WHERE userName = %s;"

        try:
            cursor.execute(query, (foodType, spiceLevel, foodPreference, sweetPreference, userName))
            connection.commit()
        except Exception:
            raise Exception
        self.databaseConnection.closeConnection()


    def getSortKeyForMenuItem(self, item, userProfile):
        # print(item)
        _, userFoodType, userSpiceLevel, userFoodPreference, userSweetPreference = userProfile
        itemID, itemName, price, availability, foodPreference, spiceLevel, vegType, isSweet = item
        


        food_preference_match = 1 if foodPreference == userFoodPreference else 0
        spice_level_match = 1 if spiceLevel == userSpiceLevel else 0
        sweet_preference_match = 1 if (userSweetPreference == isSweet) else 0
        userVegType_match = 1 if (userFoodType == vegType) else 0

        preference_score = ((food_preference_match * 3) + (spice_level_match * 2) + (sweet_preference_match * 1) + (userVegType_match * 5))
        
        # print(userProfile)
        # print(f"{userFoodType}, {vegType}")
        # preference_score = userVegType_match * 5

        return preference_score

    def sortItemAccordingToProfile(self, menuItems, userName):
        connection = self.databaseConnection.makeConnection()
        cursor = connection.cursor()

        query = "SELECT * FROM user_profile WHERE userName = %s"
        cursor.execute(query, (userName, ))
        userProfile = cursor.fetchone()

        # sortKey = self.getSortKeyForMenuItem(menuItems, userProfile)
        sortedMenuItems = sorted(menuItems, key=lambda item: self.getSortKeyForMenuItem(item, userProfile), reverse=True)
        return sortedMenuItems


if __name__ == "__main__":
    # EmployeeOperations().addVote("Mohit", "#10")
    # EmployeeOperations().addFeedback('#45', 'Manish', 4, "Pretty good")
    # EmployeeOperations().seeTodayMeal()
    # EmployeeOperations().seeNotification('Mohit')
    # EmployeeOperations().updateProfile('Mohit', 'Veg', 'Medium', 'North Indian', 'No')
    userName = 'Mohit'
    menuItems = [('#10', 'lacha paratha', '100', '1', 'North Indian', 'Low', 'Veg', 'No'), ('#99', 'Boiled Egg', '30', '1', 'North Indian', 'Low', 'Eggetarian', 'No')]

    list = EmployeeOperations().sortItemAccordingToProfile(menuItems, userName)
    print(list)
        
