__author__ = 'Dandie'

def audioSize(sec, ch, bit):
    audio_size = long(0)
    ch=int(ch)
    sec=int(sec)
    lenbit= len(bit)-1
    if len(bit)<ch:
        for i in range(lenbit+1,ch):
            bit.append(bit[lenbit])
            print i
    for bitrate in bit:
        fullrate=(bitrate*sec)/1024
        audio_size = audio_size + long(fullrate)
    print audio_size
    return audio_size