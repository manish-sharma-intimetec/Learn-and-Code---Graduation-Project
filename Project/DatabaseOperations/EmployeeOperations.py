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



if __name__ == "__main__":
    # EmployeeOperations().addVote("Mohit", "#10")
    # EmployeeOperations().addFeedback('#45', 'Manish', 4, "Pretty good")
    # EmployeeOperations().seeTodayMeal()
    # EmployeeOperations().seeNotification('Mohit')
    EmployeeOperations().updateProfile('Mohit', 'Veg', 'Medium', 'North Indian', 'No')
        
