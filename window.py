from Tkinter import *

def testing(**options):
    print "geezus"

mainWindow = Tk()
mainWindow.resizable(0,0)

audioChannels=IntVar()
audioChannels.set(1)
audioChannels.trace("w",testing)
OptimalBitrate=IntVar()
OptimalBitrate.set(0)

label = Label(mainWindow, text="Video bitrate optimizer", bd=3, fg="red").grid(row=0)

Label(mainWindow, text="Length", anchor=CENTER).grid(row=1)
movie_length=Entry(mainWindow)
movie_length.grid(row=1, column=1)

Label(mainWindow, text="Size").grid(row=2)
movie_size=Entry(mainWindow)
movie_size.grid_columnconfigure(0,weight=10)
movie_size.grid(row=2, column=1)

Label(mainWindow, text="Channels").grid(row=3)
audio_channels=Entry(mainWindow,textvariable=audioChannels)
audio_channels.grid(row=3, column=1)

Label(mainWindow, text="Channel").grid(row=4)
audio_channel=Entry(mainWindow)
audio_channel.grid(row=4, column=1)

Label(mainWindow, text="The optimal bitrate is: ").grid(row=5)
Label(mainWindow, textvariable=OptimalBitrate).grid(row=5, column=1)
Label(mainWindow, text="kbps").grid(row=5, column=2)

def callback():
    #todo: do the counting and render the return value as
    # OptimalBitrate.set('returnvalue')
    pass

b = Button(mainWindow, text="Count", command=callback)
b.grid(row=6)


mainWindow.mainloop()

