import pandas as pd
from transformers import pipeline

df = pd.read_json("resource/sampler.json")
df.shape
large_text=df[:94]
# classifier = pipeline("sentiment-analysis")
# df['sentiment']=df['text'].apply(classifier)
# print(df)
# df.to_csv('sentrest.csv')
# res=classifier("I've been waiting for a HuggingFace course my whole life.")
ner = pipeline("ner",ignore_mismatched_sizes=True ,grouped_entities=True)
df['aspect']=df['text'].apply(ner)
print(df)
df.to_csv('sentrest.csv')
