from Tkinter import *
from count import getTime, getBitratesCS

mainWindow = Tk()
mainWindow.resizable(0,0)
mainWindow.geometry('300x300')

OptimalBitrate=IntVar()
OptimalBitrate.set(0)

label = Label(mainWindow, text="Video bitrate optimizer", fg="red").pack()

Label(mainWindow, text="Length (h:m:s)", anchor=CENTER).pack()
movie_length=Entry(mainWindow)
movie_length.pack()

Label(mainWindow, text="Size (mb)").pack()
movie_size=Entry(mainWindow)
movie_size.pack()

Label(mainWindow, text="Channels (how many)").pack()
audio_channels=Entry(mainWindow,text=1)
audio_channels.pack()

Label(mainWindow, text='Channel (seperated by ",")').pack()
channelEntry = Entry(mainWindow)
channelEntry.pack()

Label(mainWindow, bg="black", fg="red", textvariable=OptimalBitrate).pack()

def countBitrate():
    seconds = getTime(movie_length.get())
    filesize = movie_size.get()
    channels = audio_channels.get()
    channel_bitrate = getBitratesCS(channelEntry.get())
    # it's an array, have to rewrite the audio counter part.
    #todo: do the counting and render the return value as
    OptimalBitrate.set(862)

b = Button(mainWindow, text="Count", command=countBitrate)
b.pack()


mainWindow.mainloop()

