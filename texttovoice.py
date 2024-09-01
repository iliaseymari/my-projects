from gtts import gTTS
from pydub import AudioSegment
import os

user = open("text.txt", 'r')
mytext = ''
language = 'en'
for line in user:
    mytext += line

myobj = gTTS(text=mytext, lang=language, slow=False)


myobj.save("output.mp3")


sound = AudioSegment.from_mp3("output.mp3")
sound = sound.speedup(playback_speed=1.5)  
sound.export("output_fast.mp3", format="mp3")




