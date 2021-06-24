from tkinter import Tk, Canvas   # tkinter library, Tk method/function
import time
import random
with open('Highscore 1.txt','r') as z:
        highscore=z.read()
a=Tk()
a.title('Falling Egg')
b=Canvas(a,width=1000,height=700,bg='#ADD8E6')
b.pack()

ground=b.create_rectangle(0,500,1000,700,fill='#6fe300')
egg=b.create_oval(450,100,510,180,fill='white')
sun=b.create_oval(200,200,-200,-200,fill='#FDB813')
basket=b.create_arc(350,350,550,480,start=180,extent=180,fill='#dbb583')

score=0
lives=5
scorecard=b.create_text(100,50,anchor='w',font='Arial 21 bold',text='Score: %s'%score)
highscore_board=b.create_text(100,70,anchor='w',font='Arial 21 bold',text='Highscore: %s'%highscore)
livescard=b.create_text(800,50,anchor='w',font='Arial 21 bold',text='Lives: %s'%lives)
def movingleft(event):
        b.move(basket,-10,0)

def movingright(event):
        b.move(basket,10,0)

b.bind('<Left>',movingleft)
b.bind('<Right>',movingright)
b.focus_set()



while True:
        e,f,g,h=b.coords(egg)
        i,j,k,l=b.coords(basket)
        b.move(egg,0,3)
        b.update()
        time.sleep(0.02)
        if i<e and g<k and h>=410:
                score=score+1
                b.itemconfig(scorecard,text='Score: %s'%score)
                x=random.randint(270,930)
                b.delete(egg)
                egg=b.create_oval(x,100,x+60,180,fill='white')
        if h>=500:
                lives=lives-1
                b.itemconfig(livescard,text='Lives: %s'%lives)
                x=random.randint(270,930)
                b.delete(egg)
                egg=b.create_oval(x,100,x+60,180,fill='white')
                if lives==0:
                        if score>int(highscore):  #30>20
                                with open('Highscore 1.txt','w') as p:
                                        p.write(str(score))  #20
                        a.destroy()
                                
