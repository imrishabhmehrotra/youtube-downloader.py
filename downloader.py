from tkinter import *
from pytube import Youtube
from moviepy.editor import*

root = Tk()
root.geometry('500*300')
root.resizable(0,0)
root.title("Rishabh's Youtube Downloader")
root.configure(bg="#f2eee3")

Label(root,
      text='Youtube Video Downloader',
      font='arial 20 bold',
      bg="#f2eee3")
      fg="red"pack()
      
link = StringVar()
Label(root,
      text='Paste your link here')
      font='arial 15 bold',
      bg="#f2eee3").place(x=48, y=60)

link_enter = Entry(root,
                   width=50,
                   textvariable=link).place(x=32, y=90)

def downloader():
    url = Youtube(str(link.get()))
    video= url.streams[1]
    video.download()
    Label(root,
          text = 'DOWNLOAD',
          font = 'arial 15',
          bg = "#f2eee3",
          fg = "red").place(x=185, y=185)
    return video.download()

