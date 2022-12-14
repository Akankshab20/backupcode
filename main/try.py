# import SentimentIntensityAnalyzer class
# from vaderSentiment.vaderSentiment module.
import csv

import pandas
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# function to print sentiments
# of the sentence.
def sentiment_scores(sentence):
    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()

    # polarity_scores method of SentimentIntensityAnalyzer
    # object gives a sentiment dictionary.
    # which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(sentence)

    print("Overall sentiment dictionary is : ", sentiment_dict)
    print("sentence was rated as ", sentiment_dict['neg'] * 100, "% Negative")
    print("sentence was rated as ", sentiment_dict['neu'] * 100, "% Neutral")
    print("sentence was rated as ", sentiment_dict['pos'] * 100, "% Positive")

    print("Sentence Overall Rated As", end=" ")

    # decide sentiment as positive, negative and neutral
    if sentiment_dict['compound'] >= 0.05:
        print("Positive")

    elif sentiment_dict['compound'] <= - 0.05:
        print("Negative")

    else:
        print("Neutral")
# csvFile = pandas.read_csv('commentary.csv')
# print(csvFile)
df = pd.read_csv("../resource/commentary.csv", "rb")
df["row_id"] = df.index + 1
df_subset = df[['row_id', 'text']].copy()
df_subset['text'] = df_subset['text'].str.replace("[^a-zA-Z#]", " ")
#covert to lower-case
df_subset['text'] = df_subset['text'].str.casefold()


print(df.shape)
df = df.head(200)
print(df.shape)






# Driver code
if __name__ == "__main__":
    print("\n1st statement :")
    print(df)
    sentence = df
#
    # function calling
    sentiment_scores(sentence)
#
#     print("\n2nd Statement :")
#     sentence = "think it's certain bowling"
#     print(sentence)
#     sentiment_scores(sentence)
#
#     print("\n3rd Statement :")
#     sentence = "And we're back with the 3rd match guys for the day"
#     print(sentence)
#     sentiment_scores(sentence)
