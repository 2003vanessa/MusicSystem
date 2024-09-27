from mutagen.mp3 import MP3

audio = MP3("Thriller.mp3") 
print(audio.info.length) 
print(audio["TIT2"].text[0])