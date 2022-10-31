# import csv
# with open('aqwerr.txt','r')as in_file:
#     stripped=(line.strip()for line in in_file)
#     lines=(line.split(",")for line in stripped if line)
#
#     with open('Austmatch.csv','w')as out_file:
#         writer=csv.writer(out_file)
#         writer.writerow(('text'))
#         writer.writerows(lines)
import csv
import json
from jsonpath_ng import jsonpath, parse

with open("../resource/whisperprocessed2.json", 'r') as json_file:
    json_data = json.load(json_file)

# print(json_data)

jsonpath_expression = parse('results[*].transcripts')

for match in jsonpath_expression.find(json_data):
    print(f'Employee id: {match.value}')

data_file = open('whisperres.csv', 'w', newline='')
csv_writer = csv.writer(data_file)

count = 0

for data in match.value:
    if count == 0:
        header = data.keys()
        csv_writer.writerow(header)
        count += 1
    csv_writer.writerow(data.values())

# import nltk
# filex = open('whisperres.csv', 'r')
# text = filex.read()
# tokens = nltk.sent_tokenize(text)
# print(tokens)
# with open(r'whisperres.csv', 'w') as fp:
#     for item in tokens:
#         # write each item on a new line
#         fp.write("%s\n" % item)
#     print('Done')
# data_file.close()

# conversion code json to csv
# with open('whisperprocessed2.json') as json_file:
#     jsondata = json.load(json_file)
#
# data_file = open('whisperprocessed2.csv', 'w', newline='')
# csv_writer = csv.writer(data_file)
#
# count = 0
# for data in jsondata:
#     if count == 0:
#         header = data.keys()
#         csv_writer.writerow(header)
#         count += 1
#     csv_writer.writerow(data.values())
# data_file.close()