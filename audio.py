def audioSize(sec, ch, bit):
    audio_size=0
    if len(bit) < ch: bit = fillAudioSlots(bit, ch)
    for bitrate in bit: audio_size += (bitrate*sec)/1024
    return audio_size

def fillAudioSlots(bit, ch):
    lenbit = len(bit)-1
    for i in range(lenbit+1,ch): bit.append(bit[lenbit])
    return bit
