# import whisper
# model = whisper.load_model("base")
# result = model.transcribe("harvard.wav", verbose=True)
# print(result["text"])

from pytube import YouTube
youtube_video_url = "https://www.youtube.com/watch?v=3haowENzdLo"
youtube_video_content = YouTube(youtube_video_url)

for stream in youtube_video_content.streams:
  print(stream)