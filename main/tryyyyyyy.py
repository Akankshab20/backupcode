import emoji
import text2emotion as te
import pandas as pd

def emotion_detection_text2emotion(x):
    all_emotions_value = te.get_emotion(x)
    Keymax_value = max(zip(all_emotions_value.values(), all_emotions_value.keys()))[1]
    return Keymax_value


data_file = pd.read_json("../resource/whisperprocessed2.json")
data_file['emotion_text2emotion'] = data_file['text'].apply(emotion_detection_text2emotion)
print(data_file['emotion_text2emotion'])
exit()
# write file
csv_data = data_file.to_csv('emot.csv')
# line_list = ['Hello World! 😄', 'Goodbye World 😅']
# new_line_list = []
#
# for word in line_list:
#   emojis = emoji.distinct_emoji_list(word)
#   new_line_list.extend([emoji.demojize(is_emoji) for is_emoji in emojis])
#   print(emojis)