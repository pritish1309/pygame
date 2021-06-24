from tkinter import Tk,Label,Entry,Button,Text,END
from datetime import datetime,date
root=Tk()
root.title('Age Calculator')
root.geometry('400x400')
x=Label(root,fg='red',text='Age Calculator')
x.grid(row=0,column=0)
name=Label(root,fg='blue', text='First Name').grid(row=1,column=0)
name_user=Entry(root)
name_user.grid(row=1,column=1)

date1=Label(root,fg='blue',text='Date of Birth').grid(row=2,column=0)
date1_user=Entry(root)
date1_user.grid(row=2,column=1)
month=Label(root,fg='blue',text='Month of Birth').grid(row=3,column=0)
month_user=Entry(root)
month_user.grid(row=3,column=1)
year=Label(root,fg='blue',text='Year of Birth').grid(row=4,column=0)
year_user=Entry(root)
year_user.grid(row=4,column=1)

# name, year, month, day --> no of days old u are as of today--> screen
def wow():
    i=date1_user.get()
    j=month_user.get()
    k=year_user.get()
    x=date.today()
    y='k,j,i'
    birthdate=date(int(k),int(j),int(i))
    age_days=x-birthdate
    print('welcome',age_days)
    t=Text(root)
    t.place(x=0,y=250)
    t.insert(END,age_days)
btn=Button(root,text='Calculate', command=wow)
btn.grid(row=5,column=0)
