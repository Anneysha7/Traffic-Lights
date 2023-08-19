from tkinter import *
import time
from threading import *
from playsound import playsound

root = Tk()

root.title("Traffic Lights")
root.geometry("200x300")

canvas = Canvas()
red = canvas.create_oval(75, 50, 125, 100, outline="black", fill="red", width=1)
green = canvas.create_oval(75, 125, 125, 175, outline="black", fill="grey", width=1)
canvas.configure(bg="black")
canvas.pack()

def threading():
    t1=Thread(target=change_colour)
    t2=Thread(target=green_play)
    t1.start()
    t2.start()

def change_colour():
    canvas.itemconfig(red, fill="grey")
    canvas.itemconfig(green, fill="green")
    start = time.time()

def green_play():
    playsound('green.mp3')

def revert():
    canvas.itemconfig(red, fill="red")
    canvas.itemconfig(green, fill="grey")

change = Button(root, text="Waiting", command=threading)
change.pack()

# background colours
root.configure(bg="black")

root.after(10250, revert)

root.mainloop()