# pip install -U spacy
# python -m spacy download en_core_web_sm
import json
from rasa_nlu.model import Metadata, Interpreter

import pandas as pd
import spacy
# Load English tokenizer, tagger, parser and NER`


nlp = spacy.load("en_core_web_sm")
df = pd.read_json("resource/sampler.json")
print(df)
df.to_string()
df.drop(["start", "end"], axis=1, inplace=True)
raw_docs = (row.text for row in df.itertuples())
# print(raw_docs)
for doc in nlp.pipe(raw_docs):

    for token in doc:
        val0= token.text, token.pos_
        # print(token.text)

    # Analyze syntax
    val1="Noun phrases:", [chunk.text for chunk in doc.noun_chunks]
    val2= "Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"]

#Find named entities, phrases and concepts
    for entity in doc.ents:
             print("text: "+entity.text, " aspect: " +entity.label_)

             dictionary = {
                 "text": entity.text,
                 "aspect": entity.label_
             }

# with open("../sample1.json", "w+") as outfile:
#               json.dump(dictionary, outfile)






#GPE - Countries, cities, states
#ORG - Companies, agencies, institutions, etc.





# text = ('This chocolate truffle cake is really tasty')
# doc = nlp(text)
#
# # Analyze syntax
# print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
# print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])
#
# for entity in doc.ents:
#     print(entity.text, entity.label_)
