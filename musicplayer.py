from pygame import mixer
from art import *

art = text2art("MUSIC", font='block', chr_ignore=True) # art for music player

print(art)

mixer.init()

# NOTE - song has to be in same directory

mixer.music.load("song.mp3")  # load song
mixer.music.set_volume(0.6)  # set volume
mixer.music.play()  # play
# mixer.music.pause()  # pause the song
# mixer.music.unpause()  # resume song
# mixer.music.set_volume(v)
# mixer.music.stop()  # stop the song

print("Welcome to the S Codes Python Music Player") # title

while True:
    print("Press 'p' to pause")
    print("Press 'r' to resume")
    print("Press 'v' to volume")  # can only be a number between 0 and 1
    print("Press 'e' to exit")

    # what happens for each option

    ch = input("['p', 'r', 'v', 'e']>>>")

    if ch == "p":
        mixer.music.pause()
    elif ch == "r":
        mixer.music.unpause()
    elif ch == "v":
        v = float(input("Enter volume(0 to 1): "))
        mixer.music.set_volume(v)
    elif ch == "e":
        mixer.music.stop()
        break
