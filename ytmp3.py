from youtube_dl import YoutubeDL
from tkinter import *
import tkinter as tk


#link = input("whats da link?: ")
window = Tk()

window.title("yt 2 mp3")

window.configure(bg = "black")


l1 = Label(window, text = "Enter your link below and press the download button", bg = 'black', fg = 'orange')
l1.grid(row = 1, column = 5)

enter_here = StringVar()
e1 = Entry(window, textvariable = enter_here,
width = 35)
e1.grid(row = 4, column = 5)
yturl = e1.get

def yt_Download():
    ydl_ye = {
        'format': 'bestaudio/best',
        'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192',}],
    }
    with YoutubeDL(ydl_ye) as ydl:
        ydl.download([e1.get()])

    

b1 = Button(window, text = "Download", command = yt_Download, fg = "orange" )
b1.grid(row = 5, column = 5)


    
window.mainloop()
   














