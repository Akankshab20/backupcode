# Load the Packages
import pandas as pd
from rasa_nlu.training_data  import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config
import spacy

# import spacy

# Loading DataSet
train_data = load_data('rasa_dataset.json')
print("1")
# Config Backend using Sklearn and Spacy
trainer = Trainer(config.load("config_spacy.yaml"))
print("2")
trainer.train(train_data)
print("3")

# Returns the directory the model is stored in (Creat a folder to store model in)
model_directory = trainer.persist('projects')
print("4")
nlp=spacy.load('en_core_web_sm')
docx = nlp(u"I am looking for an Italian Restaurant where I can eat")
for word in docx.ents:
    print("value",word.text,"entity",word.label_,"start",word.start_char,"end",word.end_char)
df = pd.read_json("resource/sampler.json")
df.to_string()
df.drop(["start", "end"], axis=1, inplace=True)
raw_docs = (row.text for row in df.itertuples())
from rasa_nlu.model import Metadata, Interpreter
interpreter = Interpreter.load(model_directory)
# for doc in nlp.pipe(raw_docs):
#     for token in doc:
#         val0= token.text, token.pos_
#
#
#
#         print((interpreter.parse(doc)))

print((interpreter.parse(u"the world's largest mining companies, Anglo-American")))