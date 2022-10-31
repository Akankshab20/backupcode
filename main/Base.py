# Importing the required libraries
import pandas as pd
import spacy
sp = spacy.load("en_core_web_sm")
from textblob import TextBlob

df = pd.read_json("../resource/sampler.json")
df.head()
df.drop(["start", "end"], axis=1, inplace=True)
print(df)

# Creating a list of positive and negative sentences.
mixed_sen = [
'They only went with five bowlers, which meant that they really needed to keep someone like Kate Cross and Sophie Eccleston for those last five or six overs.',
'This party is amazing!',
'We have come across since two matches',
'App response is very slow!'
'The trip to India was very enjoyable'
]
def asp():
    # An empty list for obtaining the extracted aspects
    # from sentences.
    ext_aspects = []

    # Performing Aspect Extraction
    for sen in mixed_sen:
            important = sp(sen)
            descriptive_item = ''
            target = ''
            for token in important:
                if token.dep_ == 'nsubj' and token.pos_ == 'NOUN':
                        target = token.text
                        print(target)
                if token.pos_ == 'ADJ':
                    added_terms = ''
                    for mini_token in token.children:
                        if mini_token.pos_ != 'ADV':
                            continue
                        added_terms += mini_token.text + ' '
                        print(added_terms)
                        descriptive_item = added_terms + token.text
            ext_aspects.append({'aspect': target,'description': descriptive_item})

    print("ASPECT EXTRACTION\n")
    print(ext_aspects)


    for aspect in ext_aspects:
     aspect['sentiment'] = TextBlob(aspect['description']).sentiment

    print("\n")
    print("SENTIMENT ASSOCIATION\n")
    print(ext_aspects)


# df['aspect'] = df['text'].apply(asp)

asp()