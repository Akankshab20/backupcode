import json
from mutagen.mp4 import MP4




#location of json file
json_source='metadata.json'
#location of video file
# video_source="chunk14.mp4"

#store json file's data into a variable
with open(json_source) as f:
   data = json.load(f)
#print(data)



#function to add metadata in video
def setMetaDataToVideo(video_source1,metadata_source1):
    try:
      video = MP4(video_source1)
    except:
        print('Video file not found')
    try:
     for k,v in metadata_source1.items():
       #print(k,v)
       video[k]=v
     video.save()
    except:
        print('Error in json/file not found')


#calling functionx
# setMetaDataToVideo(video_source,data)

def getMetaDataFromVideo(video_source):
    video = MP4(video_source)
    print(video.pprint())
    # video = TinyTag.get(video_source)
    # print(video)
    # print(video.duration)

getMetaDataFromVideo(video_source)

