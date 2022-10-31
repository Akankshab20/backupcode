import nltk
# nltk.download('punkt')
import pandas as pd
from nltk import word_tokenize
from nltk.stem.snowball import SnowballStemmer
# import requests
# from LeXmo import LeXmo
# t= """bad day"""
# emo=LeXmo.LeXmo(t)
# print(emo)

from nrclex import NRCLex

import numpy as np
import pandas as pd

text = 'Today, we put ourselves in the shoes of Cynthia Carro. Imagine youve become CEO of one of'

# Create object
emotion = NRCLex(text)

# Using methods to classify emotion
print('\n', emotion.words)
print('\n', emotion.affect_dict)
print('\n', emotion.top_emotions)

# df = pd.read_json('sampler.json')
#
# df['emotions'] = df['text'].apply(lambda x: NRCLex(x).affect_frequencies)
# df = pd.concat([df.drop(['emotions'], axis = 1), df['emotions'].apply(pd.Series)], axis = 1)
# df.drop(["start", "end"], axis=1, inplace=True)
# print(df)
# df.to_csv('emotres.csv')