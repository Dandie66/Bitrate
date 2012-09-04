from audio import audioSize
from video import countVideoBitrate

def getTime(time):
    if len(time) < 1: return 0
    time = map(int, time.split(":"))
    if len(time) == 3: return (((time[0]*60)+time[1])*60)+time[2]
    elif len(time)==2: return time[0]*60+time[1]
    elif len(time) == 1: return time[0]*60
    else: return -1

def getBitratesCS(bitrates):
    return map(int, bitrates.split(","))

def getVideoBitrate(sec,size,ch,bit):
    return countVideoBitrate(sec, size, audioSize(sec,ch,bit))