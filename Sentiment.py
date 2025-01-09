
"""
    @ Author:       Guillermo Rodriguez
    @ Created:      01/07/2025
    @ Purpose:      The purpose of this class is to consolidate sentiment scoring functionality
"""

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class sentiment:

    def __init__(self):
        self.sentiment = SentimentIntensityAnalyzer()

    def generateSentiment(self, text):
        self.text = text
        self.response = self.sentiment.polarity_scores(self.text)

    def getNegativeScore(self):
        return self.response['neg']

    def getNeutralScore(self):
        return self.response['neu']

    def getPositiveScore(self):
        return self.response['pos']

    def getCompoundScore(self):
        return self.response['compound']