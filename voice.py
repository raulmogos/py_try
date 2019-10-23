# need gTTS and mpg123
# pip install gTTS
# apt install mpg123

from gtts import gTTS
import os
from pygame import mixer

# define variables
s = str(input('enter something: '))
file = "file.mp3"

# initialize tts, create mp3 and play
tts = gTTS(s, 'ro')
tts.save(file)
os.system("mpg123 " + file)

mixer.init()
mixer.music.load("file.mp3")
mixer.music.play()
