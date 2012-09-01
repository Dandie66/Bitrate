Video Bitrate Optimizer
=======================

__DESCRIPTION:__
```
This is a program, as it helps you to calculate bitrate optimal from target filesize.
You can add for it the movie lenght, target filesize, count of audio channels and the bitrate of channels. The program's count out the video bitrate of target filsize without the audio channels. This my helps you to add data to many programs, like as Handbreake.
```
__USAGE:__
```
Run cmd, and type bitzrate.py as syntax.

Syntax:
bitrate.py <movie length minutes> <movie length sec> <target filesize in megabyte> <count of audio channels> <first audio bitrate> |second audio bitrate etc|...

movie length minutes        --> The movie lenght in minutes
movie length sec            --> The left-over seconds of movie lenght without minutes
target filesize             --> The size of file what you wanna create
count of audio channels     --> The count of audio channels what you wanna encode beside the movie
audio bitrate               --> List of bitrate of any channels what you wanna encode
```