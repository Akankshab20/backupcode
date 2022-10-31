import pandas as pd
from module import emotion5 as te
from textblob import TextBlob

df = pd.read_json("resource/sampler.json")
df.head()
# print(df.head())
def get_sentiment(text):
    blob=TextBlob(text)
    sentiment=blob.sentiment.polarity
    if sentiment>0:
        result="Positive"
    elif sentiment<0:
        result="negative"
    else:
        result="Neutral"
    return  result,sentiment

def emotion_detection_text2emotion(x):
    all_emotions_value = te.get_emotion(x)
    Keymax_value = max(zip(all_emotions_value.values(), all_emotions_value.keys()))[1]
    return Keymax_value

# df['emotion_text2emotion'] = df['text'].apply(emotion_detection_text2emotion)
# df.drop(["start", "end"], axis=1, inplace=True)
# print(df)
# df.to_csv('sentrest.csv')
# df['sentiment','cat']=df['text'].apply(get_sentiment)
# print(df)
# df.to_json('sentrest.json')
# df.to_csv('sentrest.csv')
# blog_pos=get_sentiment(' is Arka a bad boy')
blob_neg = emotion_detection_text2emotion(' try bad day')
print(blob_neg)
# print(blog_pos)


