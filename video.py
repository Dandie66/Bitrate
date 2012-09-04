def countVideoBitrate(sec,size,audio):
    return round((float((size*8)-audio)/sec)*1024,2)