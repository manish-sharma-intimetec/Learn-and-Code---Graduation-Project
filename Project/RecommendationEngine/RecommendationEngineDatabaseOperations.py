import sys
sys.path.append("..")
from DatabaseOperations.DatabaseConnection import DatabaseConnection

class RecommendationEngineDatabaseOperations:
    def __init__(self) -> None:
        self.databaseConnection = DatabaseConnection()

    def getAvgRatingForAFoodItem(self, values):
        connection = self.databaseConnection.makeConnection()
        cursor = connection.cursor()

        query = "SELECT itemID, AVG(rating) FROM feedback WHERE itemID = %s GROUP BY itemID"
        cursor.execute(query, values)
        result = cursor.fetchall()
        # print(result)

        cursor.close()
        self.databaseConnection.closeConnection()
        return result
    
    def getCommentsForAFoodItem(self, values):
        connection = self.databaseConnection.makeConnection()
        cursor = connection.cursor()

        query = "SELECT itemID, comment FROM feedback WHERE itemID = %s"
        cursor.execute(query, values)
        result = cursor.fetchall()
        # print(result)

        cursor.close()
        self.databaseConnection.closeConnection()
        return result
    

    def calculateSentimentPoints(self, itemID):
        positiveSentiments = ['good', 'nice', 'excellent', 'amazing', 'great']
        negativeSentiments = ['bad', 'poor', 'worst']
        
        result = RecommendationEngineDatabaseOperations().getCommentsForAFoodItem((itemID, ))

        sentimentScore = 0
        for (itemID, comment) in result:
            commentLower = comment.lower()
            for word in positiveSentiments:
                if word in commentLower:
                    sentimentScore += 1
            for word in negativeSentiments:
                if word in commentLower:
                    sentimentScore -= 1

        # print(sentimentScore)
        return sentimentScore



    def getTopItems(self, numberOfItems):
        connection = self.databaseConnection.makeConnection()
        cursor = connection.cursor()

        # Fetch average ratings for all items
        queryRatings = "SELECT f.itemID, m.itemName, AVG(f.rating) AS avg_rating FROM feedback f JOIN menu_item m ON f.itemID = m.itemID GROUP BY f.itemID, m.itemName;"
        cursor.execute(queryRatings)
        avgRatings = cursor.fetchall()

        cursor.close()
        self.databaseConnection.closeConnection()

        # Calculate sentiment scores for each item
        itemSentimentScores = {}
        for item in avgRatings:
            itemID = item[0]
            comments = self.getCommentsForAFoodItem((itemID,))
            sentimentScore = self.calculateSentimentPoints(itemID)
            itemSentimentScores[itemID] = sentimentScore

        # Combine average rating and sentiment score
        combinedScores = [
            (item[0], item[1], itemSentimentScores[item[0]])
            for item in avgRatings
        ]

        # Sort items based on combined score (average rating + sentiment score)
        combinedScores.sort(key=lambda x: (x[1], x[2]), reverse=True)

        # Return top items
        topItems = combinedScores[:numberOfItems]
        # print(topItems)
        return topItems

    

if __name__ == "__main__":
    obj = RecommendationEngineDatabaseOperations()
    # obj.getAvgRatingForAFoodItem(('#1', ))
    # obj.getCommentsForAFoodItem(('#1', ))
    obj.getTopItems(2)