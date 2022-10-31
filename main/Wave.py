import wave, math, contextlib
import speech_recognition as sr
# from moviepy.editor import AudioFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip

transcribed_audio_file_name = "../resource/aust.wav"
zoom_video_file_name = "../resource/AustraliaVsBangladesh.mp3"
# zoom_video_file_name = "audio-chunks/chunk1.wav"

audioclip = AudioFileClip(zoom_video_file_name)
audioclip.write_audiofile(transcribed_audio_file_name)
with contextlib.closing(wave.open(transcribed_audio_file_name,'r')) as f:
    frames = f.getnframes()
    rate = f.getframerate()
    duration = frames / float(rate)
total_duration = math.ceil(duration / 60)
r = sr.Recognizer()
for i in range(0, total_duration):
    with sr.AudioFile(transcribed_audio_file_name) as source:
        audio = r.record(source, offset=i*60, duration=60)
    f = open("../resource/transcription.txt", "a")
    f.write(r.recognize_google(audio))
    f.write(" ")
f.close()