from tkinter import Tk,Text
from datetime import datetime,date
root=Tk()
root.withdraw()
x=date.today()
special_dates={}
with open('dates.txt','r') as f:
    for k in f:
        line=k.rstrip('\n')
        g,h=line.split(':')
        y=datetime.strptime(h,'%d/%m/%y').date()
        time_left=str(y-x)
        final=time_left.split(',')
        special_dates[g]=final[0]
        print('Time left for ',g,'is',final[0])
        




