import pandas as pd
import spacy
import text2emotion as te
from textblob import TextBlob


# print(df.head())
def get_sentiment(text):
    try:
        blob=TextBlob(text)
        sentiment=blob.sentiment.polarity
        if sentiment>0:
            result="Positive"
        elif sentiment<0:
            result="negative"
        else:
            result="Neutral"
        return  result,sentiment
    except Exception as e:
        print("Failed to extract sentiments", e)

def emotion_detection_text2emotion(x):
    try:
        all_emotions_value = te.get_emotion(x)
        Keymax_value = max(zip(all_emotions_value.values(), all_emotions_value.keys()))[1]
        return Keymax_value
    except Exception as e:
        print("Failed to extract emotions ", e)



def aspectanalysis(text):

    try:

        # print(text)
        # df = pd.read_json("file")
        nlp = spacy.load("en_core_web_sm")

        final_list = []
        # # for doc in nlp.pipe(text):
        #     print(doc)
        #     for token in doc:
        #         val0 = token.text, token.pos_


            # Analyze syntax
            # val1 = "Noun phrases:", [chunk.text for chunk in doc.noun_chunks]
            # val2 = "Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"]

            # Find named entities, phrases and concepts
        print(text)
        response = nlp(text)
        print(response.ents)
        for entity in response.ents:
        # for entity in doc.ents:
        #     print(entity)
        #     print("text: " + entity.text, " aspect: " + entity.label_)
            dictionary = {
                    "text": entity.text,
                    "aspect": entity.label_
                }
        # 
        #     pop = pd.Series(dictionary)
        #     #print(pop)
            final_list.append(dictionary)
        return final_list
    except Exception as e:
        print("Failed to extract aspect ", e)



def sentimentanalysis(file):

    df = pd.DataFrame.from_dict(file)
    # df.head()
    df.drop(["start", "end"], axis=1, inplace=True)
    df['aspect_analysis']=df['text'].apply(aspectanalysis)
    df['emotion_text2emotion'] = df['text'].apply(emotion_detection_text2emotion)

    print(df)

    df['sentiment','cat']=df['text'].apply(get_sentiment)
    print(df)

    rest=df.to_json('sentrest.json')
    df.to_csv('sentrest.csv')
    return df.to_json()

