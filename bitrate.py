#!/usr/bin/python
# coding=UTF-8
import sys
from count import getTime, getBitratesCS, getVideoBitrate
from display import *

channels, audio_output_filesize = [], 0
try:
    if sys.argv[1] == "--help":
        help()
    else:
        video_bitrate = getVideoBitrate(getTime(sys.argv[1]),float(sys.argv[2]),int(sys.argv[3]),getBitratesCS(sys.argv[4]))
        if video_bitrate < 0: tooSmall()
        elif video_bitrate < 750: lowBitrate(video_bitrate)
        else: optimalBitrate(video_bitrate)
except IndexError:
    import window