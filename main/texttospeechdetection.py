import pandas as pd
from nltk.metrics import scores

from pattern.text.en import sentiment
df = pd.read_json("../resource/whisperprocessed2.json")
df.to_string()

# df.drop(["start", "end"], axis=1, inplace=True)
# for index, row in df.iterrows():
#
#         sentiment_scores=sentiment(row["text"])
#
#         sentiment_category = ['positive' if score > 0
#                                               else 'negative' if score < 0
#                                                   else 'neutral'
#                                                       for score in sentiment_scores]
#
#         values = {'text': [row["text"]],'sentiment_category': [sentiment_category[0]],'sentiment_score': [sentiment_scores[0]]}
#         print(values)
#         df = pd.DataFrame(values)
# print(df)
# df.to_json('sentrest1.csv')

sentiment_scores = sentiment('Boys will be boys, they commit mistakes')
print(sentiment_scores)




