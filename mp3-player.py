# A simple mp3 player

from pydub import AudioSegment
from pydub.playback import play
import pydub.playback
import pyaudio, wave
import subprocess
import time

music_file = 'music.mp3'

song = AudioSegment.from_mp3(music_file)

#chunk = 1024
#wf = wave.open('output.wav', 'rb')
#song.export('music_wav.wav', format='wav')

#subprocess.call(['ffmpeg', '-i', music_file, 'output.wav'])


beginning = song[:5000] - 10
end = song[-5000:] - 10
new_song = beginning + end

def covert_milliseconds(millis):
    seconds = (millis/1000)%60
    seconds = int(seconds)
    minutes = (millis/(1000*60))%60
    minutes = int(minutes)
    #hours = (millis/(1000*60*60))%24
    #hours = int(hours)

    # add leading zeroes if the numbers only consists of one digit
    if len(str(seconds)) == 1:
        seconds = '0' + str(seconds)

    if len(str(minutes)) == 1:
        minutes = '0' + str(minutes)

    #return ('%s:%s:%s' % (hours, minutes, seconds))
    return ('%s:%s' % (minutes, seconds))

print(covert_milliseconds(len(song)))

'''
while True:
    try:
        play(song)
    except KeyboardInterrupt:
        print('stopping song')
        break
'''
play(song)
#pydub.playback._play_with_pyaudio(song)

'''
p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()), channels=wf.getnchannels(), rate=wf.getframerate(), output=True)

data = wf.readframes(chunk)

while data != '':
    stream.write(data)
    data = wf.readframes(chunk)

time.sleep(5)

stream.close()
p.terminate()
'''