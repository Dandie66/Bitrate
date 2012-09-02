def getTime(time):
    """ returns the given time in seconds """
    time = time.split(":")
    time[0] = int(time[0])
    time[1] = int(time[1])
    time[2] = int(time[2])
    if len(time) == 3:
        return (((time[0]*60)+time[1])*60)+time[2]
    elif len(time) == 2:
        return (time[0]*60)+time[1]
    else:
        return time[0]

def getBitratesCS(bitrates):
    bitrates = bitrates.split(",")
    return bitrates