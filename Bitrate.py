#!/usr/bin/python
import sys

channels=[]
audio_output_filesize = 0

#sys.argv[1] == "" criterion not interpreted. Create an error under Windows.
if sys.argv[1] == "--help" or sys.argv[1] == "":
    print "<movie length minutes> <movie length sec> <target filesize in megabyte> <count of audio channels> <first audio bitrate> <second audio bitrate> etc..."

else:
    movie_length    = (float(sys.argv[1])*60) + float(sys.argv[2])
    movie_filesize    = float(sys.argv[3])*8
    audio_channels    = float(sys.argv[4])
    for i in range(5,int(5+audio_channels)):
        try:
            audio_output_filesize += (movie_length*float(sys.argv[i]))/1024
        except IndexError:
            break

    if movie_filesize < audio_output_filesize:
        print "-- That file size is too small for a video encoding, the audio size is by itself %.0fmb" % (audio_output_filesize/8)
    else:
        video_bitrate = ( (movie_filesize-audio_output_filesize)/movie_length)*1024
        if video_bitrate < 750:
            print "-- WARNING! The quality is low, but the bitrate for this conversion is: %.0f" % video_bitrate
        else:
            print "-- The recommended bitrate for this kind of conversion: %.0f" % video_bitrate
