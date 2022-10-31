import csv
import re
import nltk
filex = open('AustVsBan.txt', 'r')
text = filex.read()
tokens = nltk.sent_tokenize(text)
print(tokens)
with open(r'aqwerr.txt', 'w') as fp:
    for item in tokens:
        # write each item on a new line
        fp.write("%s\n" % item)
    print('Done')