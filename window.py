from Tkinter import *
from count import get_Time, getBitratesCS, countingRate

mainWindow = Tk()
mainWindow.resizable(0,0)
mainWindow.geometry('300x300')

OptimalBitrate=IntVar()
OptimalBitrate.set(0)

label = Label(mainWindow, text="Video bitrate optimizer", fg="red").pack()

Label(mainWindow, text="Length (h:m:s)", anchor=CENTER).pack()
movie_length=Entry(mainWindow, text="115:16")
movie_length.pack()

Label(mainWindow, text="Size (mb)").pack()
movie_size=Entry(mainWindow, text="1400")
movie_size.pack()

Label(mainWindow, text="Channels (how many)").pack()
audio_channels=Entry(mainWindow,text=2)
audio_channels.pack()

Label(mainWindow, text='Channel (seperated by ",")').pack()
channelEntry = Entry(mainWindow, text="448")
channelEntry.pack()

Label(mainWindow, bg="black", fg="red", textvariable=OptimalBitrate).pack()

def countBitrate():
    seconds = int(get_Time(movie_length.get()))
    filesize = int(movie_size.get())
    channels = int(audio_channels.get())
    channel_bitrate = getBitratesCS(channelEntry.get())
    OptimalBitrate.set(countingRate(seconds,filesize,channels,channel_bitrate))

b = Button(mainWindow, text="Count", command=countBitrate)
b.pack()

mainWindow.mainloop()

