Video Bitrate Optimizer
=======================

__DESCRIPTION:__
```
This is a program, it helps you to calculate the optimal bitrate for the target filesize.
You can add the movie length, target filesize, count of audio channels and the bitrate of channels.
The program's counts out the video bitrate of target filsize without the audio channels.
This might help you to add data to various programs, like Handbreake for example.
```
__USAGE:__
Run the command, and type `python bitrate.py` as syntax.

Syntax:
```
python bitrate.py <movie length minutes> <movie length sec> <target filesize in megabyte>
<count of audio channels> <first audio bitrate> |second audio bitrate etc|...
```

```
movie length minutes        --> The movie length in minutes
movie length sec            --> The left-over seconds of movie length without minutes
target filesize             --> The size of file you would like to create
count of audio channels     --> The count of audio channels what you would like to encode beside the movie
audio bitrate               --> List of bitrate of any channels what you would like to encode
```