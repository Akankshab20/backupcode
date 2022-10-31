import os

import whisper
import json
from datetime import datetime

sourceOfVideo="" #source location
video_name="sample.mp4" #video name
subtitle_destination="whisper-result-processed2.json" #the complete json destination including json file name

def getSubtitles(sourceOfvideo,video_name,subTitle_dest ):
    #video=sourceOfvideo+video_name
    try:
      video=os.path.join(sourceOfvideo, video_name)
      model = whisper.load_model("base") #medium
    except:
      print("video not found")
      #print("1- " + str(datetime.now()))
    result = model.transcribe(video) #get video from s3
    #print("2- " + str(datetime.now()))
    #print(result["text"])
    #print(result)
    data = result
    segments = data['segments']
    processed_data = []
    for item in segments:
        obj = {
            "text": item.get('text'),
            "start": item.get('start'),
            "end": item.get('end')
        }
        processed_data.append(obj)
    #write processed data into json
    with open(subTitle_dest, 'w') as f:
        json.dump(processed_data, f)


getSubtitles(sourceOfVideo,video_name,subtitle_destination)
#this code will run only from command line
#python3 whisper_setup.py



