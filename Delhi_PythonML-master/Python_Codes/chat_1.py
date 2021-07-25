from datetime import datetime as dt
import os, random, glob

hello_intent = ["hello", "hi", "hey", "hello there", "hi there"]
date_intent = ["tell me date","today's date","date","what's the date"]
time_intent = ["tell me time","current time","time","what's the time"]
musicIntent = ["play music","play song"]

while True:
    msg = input("Enter your message : ")

    if msg in hello_intent:
        print("Hello User")
    elif msg in date_intent:
        d = dt.now().date()
        print(d.strftime("%d/%m/%y,%a"))
    elif msg in time_intent:
        t = dt.now().time()
        print(t.strftime("%H:%M:%S,%p"))
    elif msg in musicIntent:
        os.chdir(r'C:\Users\asus\Music')
        songs = glob.glob('*.mp3')
        random_song = random.choice(songs)
        os.startfile(random_song)
    elif msg == "songs":
        os.chdir(r'C:\Users\asus\Music')
        songs = glob.glob('*.mp3')
        '''
        for i in range(len(songs)):
            print(songs[i])
        '''

        for i,song in enumerate(songs):
            print(i, song)
        ch = input("Enter the track number : ")
        
    elif msg == "bye":
        print("Bye User")
        break
    else:
        print("I don't understand")















