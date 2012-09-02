#!/usr/bin/python
import sys

# Csak hogy értsd mi ez az import, from display = a display.py-ből, importálja be a help, tooSmall stb. függvényeket.
# Ha megértetted hogy müködik, akkor majd írd át *-ra az import utánit, az az import minden.
# Próbálom picit objektum orientáltabbá tenni, hogy könyebb legyen ketten beledolgozni :)
# Még szétlehetne jobban szedni, de nem akarlak annyira megzavarni, így kapásból.
from display import help, tooSmall, lowBitrate, optimalBitrate

channels, audio_output_filesize = [], 0

try:
    if sys.argv[1] == "--help":
        help()
    else:
        movie_length    = (float(sys.argv[1])*60) + float(sys.argv[2])
        movie_filesize    = float(sys.argv[3])*8
        audio_channels    = float(sys.argv[4])
        for i in range(5,int(5+audio_channels)):
            try:
                audio_output_filesize += (movie_length*float(sys.argv[i]))/1024
            except IndexError:
                audio_output_filesize += (5+audio_channels-i)*(movie_length*float(sys.argv[i-1]))/1024
                break

        if movie_filesize < audio_output_filesize:
            tooSmall(audio_output_filesize/8)
        else:
            video_bitrate = ( (movie_filesize-audio_output_filesize)/movie_length)*1024
            if video_bitrate < 750:
                lowBitrate(video_bitrate)
            else:
                optimalBitrate(video_bitrate)
except IndexError:
    help()