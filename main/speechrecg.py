import statistics

import numpy
import pytz

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from numpy import dtype

filename='HuflixFe.Wav'
import librosa
import pandas as pd
import matplotlib.pyplot as plt
x, sr = librosa.load(filename,sr=16000)
int(librosa.get_duration(x, sr)/60)
max_slice=5
window_length = max_slice * sr

# import IPython.display as ipd
# a=[21*wixndow_length:22*window_length]
# ipd.Audio(a, rate=sr)

# energy1 = sum(abs(a**2))
# # print(energy)
# len(a)
# import matplotlib.pyplot as plt
# fig = plt.figure(figsize=(14, 8))
# ax1 = fig.add_subplot(211)
# ax1.set_xlabel('time')
# ax1.set_ylabel('Amplitude')
# ax1.plot(a)
import numpy as np
try:
    energy = np.array([sum(abs(x[i:i+window_length]**2)) for i in range(0, len(x), window_length)])
    print(len(x))
    print(energy)
    print("done")
except ValueError as e:
    print(e)

# plt.hist(energy)
# plt.show()
# print("done1")

df=pd.DataFrame(columns=['energy','start','end'])
# thresh=500
# thresh=numpy.mean(energy)
# print(thresh)
threshold= np.mean(energy) + 2 * np.std(energy)
# print(np.mean(energy))
thresh=np.ceil(threshold)
print(thresh)
# print(threshold)
# 3000
# print("a1")
row_index=0
# print("a2")
print(len(energy))
try:
    for i in range(len(energy)):
        value=energy[i]
        if(value>=thresh):
            i=np.where(energy == value)[0]
            # print("a2")

            df.loc[row_index,'energy']=value
            # print("a3")
            df.loc[row_index,'start']=(i[0] * max_slice)-5
            df.loc[row_index,'end']=(i[0]+1) * max_slice
            row_index= row_index + 1
    print(df)
except:
    print('not able to get exciment level')

temp=[]
i=0
j=0
n=len(df) - 2
m=len(df) - 1
try:
    while(i<=n):
      j=i+1
      while(j<=m):
        if(df['end'][i] >= df['start'][j]):
          df.loc[i,'end'] = df.loc[j,'end']
          temp.append(j)
          j=j+1
        else:
          i=j
          break
except:
    print('Not able to append the start and end time')
df.drop(temp,axis=0,inplace=True)
print(df)
# print(dtype(df['start']))
# df['start'] = df['start'].astype(int).astype('datetime64[s]')
# df['end'] = df['end'].astype(int).astype('datetime64[s]')
# print(df)

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
start=np.array(df['start'])
end=np.array(df['end'])
try:
    for i in range(len(df)):
     if(i!=0):
      start_lim = start[i] - 5
     else:
      start_lim = start[i]
     end_lim   = end[i]
     filename="chunk" + str(i+1) + ".mp4"
     ffmpeg_extract_subclip("../resource/HuflixFe-highlight.mp4", start_lim, end_lim, targetname=filename)
    # # # # df.to_csv('Austout.csv')
except:
    print('not able to crop the video')


