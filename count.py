def getTime(time):
    """ returns the given time in seconds """
    if len(time) < 1:
        return 0

    time = time.split(":")
    map(int, time)

    if len(time) == 3:
        return (((time[0]*60)+time[1])*60)+time[2]
    elif len(time) == 2:
        return (time[0]*60)+time[1]
    elif len(time) == 1:
        return time[0]
    else:
        return -1

def getBitratesCS(bitrates):
    bitrates = bitrates.split(",")
    return bitrates

def CountingRate(sec, size, ch, bit):
