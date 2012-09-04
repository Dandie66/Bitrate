from Tkinter import *
from count import getTime, getBitratesCS, getVideoBitrate

mainWindow = Tk()
mainWindow.resizable(0,0)
mainWindow.geometry('300x300')

OptimalBitrate=IntVar()
OptimalBitrate.set(0)

label = Label(mainWindow, text="Video bitrate optimizer", fg="red").pack()

Label(mainWindow, text="Length (h:m:s)", anchor=CENTER).pack()
movie_length=Entry(mainWindow)
#movie_length.insert(0,"115:16")
movie_length.pack()

Label(mainWindow, text="Size (mb)").pack()
movie_size=Entry(mainWindow)
#movie_size.insert(0, 1400)
movie_size.pack()

Label(mainWindow, text="Channels (how many)").pack()
audio_channels=Entry(mainWindow)
#audio_channels.insert(0, 2)
audio_channels.pack()

Label(mainWindow, text='Channel (seperated by ",")').pack()
channelEntry = Entry(mainWindow)
#channelEntry.insert(0, 448)
channelEntry.pack()

Label(mainWindow, bg="black", fg="red", textvariable=OptimalBitrate).pack()

def countBitrate():
    OptimalBitrate.set(getVideoBitrate(int(getTime(movie_length.get())),int(movie_size.get()),int(audio_channels.get()),getBitratesCS(channelEntry.get())))

b = Button(mainWindow, text="Count", command=countBitrate)
b.pack()

mainWindow.mainloop()

