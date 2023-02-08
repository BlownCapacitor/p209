import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
from playsound import playsound
import pygame
from pygame import mixer
import os
import time

song_counter = 0
result_counter = 0
PORT  = 8080
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096
selected_song = None
searchQuery = None

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))
    openChatWindow()

def get_songs():
    global song_counter

    for file in os.listdir('shared_files'):
        filename = os.fsdecode(file)
        listbox.insert(song_counter, filename)
        song_counter = song_counter + 1

def play():
    global selected_song
    selected_song = listbox.get(ANCHOR)
    pygame
    mixer.init()
    mixer.music.load('shared_files/'+selected_song)
    mixer.music.play()
    if(selected_song != ""):
        infoLabel.configure(text = "Now Playing: " + selected_song)
    else:
        infoLabel.configure(text = "")

def stop():
    global selected_song
    pygame
    mixer.init()
    mixer.music.load('shared_files/'+selected_song)
    mixer.music.pause()
    infoLabel.configure(text = "")

def search():
   global resultbox
   global searchQuery
   global result_counter
   result = []
   for root, dir, files in os.walk('shared_files'):
      if searchQuery in files:
         result.append(os.path.join(root, searchQuery))
         resultbox.insert(result_counter, result)
         result_counter = result_counter + 1
   
def openChatWindow():
    global infoLabel
    global listbox
    global resultbox
    global searchQuery
    window=Tk()
    window.title('LAN Music Sharing')
    window.geometry("500x350")
    window.configure(bg = '#ccffee')
    
    photo = PhotoImage(file = "pause.png")
    photoimage = photo.subsample(7, 7)

    photo2 = PhotoImage(file = "play.png")
    photoimage2 = photo2.subsample(13, 13)

    photo3 = PhotoImage(file = "search.png")
    photoimage3 = photo3.subsample(4, 4)

    selectlabel = Label(window, text= "Select a Song:", bg = '#ccffee', font = ("Calibri",15))
    selectlabel.place(x=2, y=1)

    searchlabel = Label(window, text= "Or Search:", bg = '#ccffee', font = ("Calibri",15))
    searchlabel.place(x=300, y=1)

    searchbar  = Entry(window, bg = "white", font = ("Calibri", 10))
    searchbar.place(x= 300, y = 30)
    searchQuery = searchbar.get()
    listbox = Listbox(window,height=10, width=39, activestyle = 'dotbox', bg = '#ccffee', borderwidth=2, font = ("Calibri", 10))
    listbox.place(x=10,y=30)
    
    resultbox = Listbox(window,height=8, width=25, activestyle = 'dotbox', bg = '#ccffee', borderwidth=2, font = ("Calibri", 10))
    resultbox.place(x=300,y=50)
    
    searchButton = Button(window, image = photoimage3, compound = CENTER, command = search)
    searchButton.place(x= 450, y = 30)


    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight=1, relx = 1)
    scrollbar1.config(command=listbox.yview)

    scrollbar2 = Scrollbar(resultbox)
    scrollbar2.place(relheight=1, relx = 1)
    scrollbar2.config(command=resultbox.yview)

    playButton = Button(window, text="Play", bd= 1, bg= "#ddffee", font = ("Calibri",10), image = photoimage2, compound = LEFT, command = play)
    playButton.pack(side = TOP)
    playButton.place(x=30,y=220)
    
    Stop = Button(window, text= "Pause", bd=1, bg="#ddffee", font = ("Calibri", 10), image = photoimage, compound = LEFT, command = stop)
    Stop.pack(side = TOP)
    Stop.place(x=200, y=220)
  
    Upload =Button(window, text="Upload", width=10, bd = 1, bg ='#ddffee', font = ("Calibri", 10))
    Upload.place(x=30, y=280)

    Download =Button(window, text="Download", width=10, bd = 1, bg ='#ddffee', font = ("Calibri", 10))
    Download.place(x=200, y=280)

    infoLabel = Label(window, text="", fg = "blue", font = ("Calibri", 8))
    infoLabel.place(x=50, y = 320)
    get_songs()
    window.mainloop()

setup()