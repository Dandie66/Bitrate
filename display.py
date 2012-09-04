def help():
    """ Display a help message """
    print "<movie length minutes> <movie length sec> <target filesize in megabyte> <count of audio channels> <first audio bitrate> <second audio bitrate> etc..."

def tooSmall():
    """ Display a message that the audio size is bigger then the preferred video size """
    print "-- That file size is too small for a video encoding, the audio size is by itself"

def lowBitrate(bitrate):
    """ Display a message that the video quality would be low for this size """
    print "-- WARNING! The quality is low, but the bitrate for this conversion is: %.0f" % bitrate

def optimalBitrate(bitrate):
    """ Displays the optimal bitrate """
    print "-- The recommended bitrate for this kind of conversion: %.0f" % bitrate