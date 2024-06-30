import sys
sys.path.append("..")

from RecommendationEngine.RecommendationEngineDatabaseOperations import RecommendationEngineDatabaseOperations

class RecommendationEngine:
    
    def getAvgRating(self, itemID):
        result = RecommendationEngineDatabaseOperations().getAvgRatingForAFoodItem((itemID, ))

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

        print(sentimentScore)
        return itemID ,sentimentScore


    def getTopItems(self, numberOfItems):
        result = RecommendationEngineDatabaseOperations().getTopItems(numberOfItems)

        print(result)
        

if __name__ == "__main__":
    obj = RecommendationEngine()
    # obj.calculateSentimentPoints('#1')
    # obj.getAvgRating('#1')
    obj.getTopItems(2)
