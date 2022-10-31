import re
# import pandas as pd
import matplotlib.pyplot as plt
import nltk
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
# nltk.download('vader_lexicon')
#df = pd.read_excel (r'Path where the Excel file is stored\File name.xlsx')
# df = pd.read_csv("whisperprocessed2.csv","rb")
columns = ["text"]
df = pd.read_csv("../resource/whisperprocessed2.csv", usecols=columns)
# adding an row_id field to the dataframe, which will be useful for joining later
df["row_id"] = df.index + 1
#print first 10 rows
print (df)
#create a new data frame with "id" and "comment" fields
df_subset = df[['row_id', 'text']].copy()
print(df_subset)
#data clean-up
#remove all non-aphabet characters
df_subset['text'] = df_subset['text'].str.replace("[^a-zA-Z#]", " ")
#covert to lower-case
df_subset['text'] = df_subset['text'].str.casefold()
print (df_subset)
df1=pd.DataFrame()
# print(df1)
df1['row_id']=['99999999999']
df1['sentiment_type']='NA999NA'
df1['sentiment_score']=0
print('Processing sentiment analysis...')
sid = SentimentIntensityAnalyzer()
t_df = df1
def get_sentiment(row):
    sentiment_dict = sid.polarity_scores(row)
    print("Overall sentiment dictionary is : ", sentiment_dict)
    print("sentence was rated as ", sentiment_dict['neg'] * 100, "% Negative")
    print("sentence was rated as ", sentiment_dict['neu'] * 100, "% Neutral")
    print("sentence was rated as ", sentiment_dict['pos'] * 100, "% Positive")
    result = " "
    # print("Sentence Overall Rated As", end=" ")
    if sentiment_dict['compound'] >= 0.05:
        print("Positive")
        result = "pos"
    elif sentiment_dict['compound'] <= - 0.05:
        print("Negative")
        result = "neg"
    else:
        print("Neutral")
        result = "neu"
    return sentiment_dict,result

for index, row in df_subset.iterrows():

     scores,Key = get_sentiment(row["text"])
     # print(scores)
     print(row["text"])
     for key, value in scores.items():
         if Key == key:
             # print(key)
             temp = [key, value, row[0]]
             df1['row_id'] = row[0]
             df1['sentiment_type'] = key
             df1['sentiment_score'] = value
             # df1['test']=row["text"]
             t_df = t_df.append(df1)

# remove dummy row with row_id = 99999999999
t_df_cleaned = t_df[t_df.row_id != '99999999999']
# # #remove duplicates if any exist
t_df_cleaned = t_df_cleaned.drop_duplicates()
# t_df_cleaned = t_df.drop_duplicates()
# t_df_cleaned = t_df[t_df.sentiment_type == 'compound']
print(t_df_cleaned)
