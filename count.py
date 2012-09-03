from audio import *
from display import *

def get_Time(time):
    if len(time) < 1:
        return 0

    time = time.split(":")
    map(int, time)

    if len(time) == 3:
        return (((time[0]*60)+time[1])*60)+time[2]
    elif len(time) <= 2:
        if len(time)==2:
            return time[0]*60+time[1]
        elif len(time) == 1:
            return time[0]*60
    else:
        return -1

def getBitratesCS(bitrates):
    bitrates = bitrates.split(",")
    return bitrates

def countingRate(sec,size,ch,bit):
   audio = audioSize(sec,ch,bit)
   video_bitrate=0
   if size < audio:
       tooSmall(audio/8)
   else:
       video_bitrate = ((size-audio)/sec)*1024
       if video_bitrate < 750:
           lowBitrate(video_bitrate)
       else:
           optimalBitrate(video_bitrate)
   return video_bitrate