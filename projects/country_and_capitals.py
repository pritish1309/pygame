from tkinter import Tk,simpledialog,messagebox
root=Tk()
root.withdraw()
capitals={}
with open('capitals.txt','r') as f:
    for k in f:
        line=k.rstrip('\n')     #'India:New Delhi\n
        g,h=line.split(':')
        capitals[g]=h

#x=input('Enter the name of a country to find out its capital : ')
while True:
    x=simpledialog.askstring('Question','Enter a Country Name')
    if x in capitals:
        messagebox.showinfo('Answer',capitals[x])
    else:
        y=simpledialog.askstring("Enlighten Us","Please enter the country's capital you asked")
        capitals[x]=y
        with open('capitals.txt','a') as p:
            single='\n'+x+':'+y
            p.write(single)
            
    
