"""
    @ Author:       Guillermo Rodriguez
    @ Created:      01/07/2025
    @ Purpose:      Process a series of inputs from a designated file to determine if the line entry provided is either:
                        1. POSITIVE
                        2. NEUTRAL
                        3. NEGATIVE
                    THe program is an example of sentiment analysis using LLMs i
"""

from Sentiment import sentiment

if __name__ == "__main__":
    print("Started ....")

    # Constants
    INPUT_FILE = './Data/Sentiment/sentiment.data'
    
    # Variables
    derived_sentiment = sentiment()
    total_score = 0

    # Processing
    with open(INPUT_FILE, 'r') as data:
        for line in data:
            derived_sentiment.generateSentiment(line.strip())

            print(line.strip() + " : " + str(derived_sentiment.getCompoundScore()) )

            total_score += derived_sentiment.getCompoundScore()

    print("The total sentiment of the document is: " + str(total_score))

    if total_score > 0:
        print("The document is positive")
    elif total_score < 0:
        print("The document is negative")
    else:
        print("The document is neutral")

    print("Completed ....")