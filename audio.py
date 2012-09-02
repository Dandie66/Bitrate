from window import *
__author__ = 'Dandie'

from Tkinter import *
from count import *

def audioSize(sec, ch, bit=[]): #bit - array
    if len(bit)<ch:
        for i in range(len(bit)+1,ch):
            bit(i) = bit(len(bit))
        for i in range(1, ch):
            audio_size += (sec*float(bit(i)))/1024
    return audio_size