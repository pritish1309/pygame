from tkinter import Tk,Canvas,PhotoImage
import time
import random
root=Tk()
canvas=Canvas(root,width=500,height=500,bg='black')
canvas.pack()
g=PhotoImage(file='gem.png')
gem=canvas.create_image(250,50,image=g)

def moving():
    canvas.move(gem,x,y)
    canvas.update()
    time.sleep(0.01)

speed1=1
speed2=1

while True:
    x,y=5,7
    x=x*speed1
    y=y*speed2
    moving()
    a,b=canvas.coords(gem)
    print(a,b)
    if a>=500 :
        speed1=-1
    elif a<=0 :
        speed1=1
    if b>=500 :
        speed2=-1
    elif b<=0:
        speed2=1
