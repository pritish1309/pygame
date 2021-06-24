from tkinter import Tk,Canvas,NORMAL,HIDDEN, PhotoImage
root=Tk()
a=Canvas(root,height=700,width=700)
a.pack()

# photoimages of all the pictures
q=PhotoImage(file='sad emoji.png')
n=PhotoImage(file='angry emoji.png')
o=PhotoImage(file='happy emoji.png')
r=PhotoImage(file='blush emoji.png')
s=PhotoImage(file='party emoji.png')
t=PhotoImage(file='angry emoji cuss.png')


#4 functions to be created
#for angry face on double clicking the emoji
def angry_face1(event):
    angry_emoji=a.create_image(350,350,image=n,state=NORMAL)
    sad_emoji=a.create_image(350,350,image=q,state=HIDDEN)
    happy_emoji=a.create_image(350,350,image=o,state=HIDDEN)
    party_emoji=a.create_image(350,350,image=s,state=HIDDEN)
    blush_emoji=a.create_image(350,350,image=r,state=HIDDEN)
    angry_emoji_cuss=a.create_image(350,350,image=t,state=HIDDEN)

#for happy face on moving mouse
def happy_face(event):
    happy_emoji=a.create_image(350,350,image=o,state=NORMAL)
    sad_emoji=a.create_image(350,350,image=q,state=HIDDEN)
    angry_emoji=a.create_image(350,350,image=n,state=HIDDEN)
    party_emoji=a.create_image(350,350,image=s,state=HIDDEN)
    blush_emoji=a.create_image(350,350,image=r,state=HIDDEN)
    angry_emoji_cuss=a.create_image(350,350,image=t,state=HIDDEN)

#for sad face on leaving the sreen
def sad_face(event):
    sad_emoji=a.create_image(350,350,image=q,state=NORMAL)
    angry_emoji=a.create_image(350,350,image=n,state=HIDDEN)
    happy_emoji=a.create_image(350,350,image=o,state=HIDDEN)
    party_emoji=a.create_image(350,350,image=s,state=HIDDEN)
    blush_emoji=a.create_image(350,350,image=r,state=HIDDEN)
    angry_emoji_cuss=a.create_image(350,350,image=t,state=HIDDEN)

#for a blushing face on pressing the scroll wheel button
def blush_face(event):
    blush_emoji=a.create_image(350,350,image=r,state=NORMAL)
    sad_emoji=a.create_image(350,350,image=q,state=HIDDEN)
    angry_emoji=a.create_image(350,350,image=n,state=HIDDEN)
    happy_emoji=a.create_image(350,350,image=o,state=HIDDEN)
    party_emoji=a.create_image(350,350,image=s,state=HIDDEN)
    blush_emoji=a.create_image(350,350,image=r,state=HIDDEN)
    angry_emoji_cuss=a.create_image(350,350,image=t,state=HIDDEN)

#for a party face on pressing the right click button
def party_face(event):
    party_emoji=a.create_image(350,350,image=s,state=NORMAL)
    sad_emoji=a.create_image(350,350,image=q,state=HIDDEN)
    angry_emoji=a.create_image(350,350,image=n,state=HIDDEN)
    happy_emoji=a.create_image(350,350,image=o,state=HIDDEN)
    blush_emoji=a.create_image(350,350,image=r,state=HIDDEN)
    angry_emoji_cuss=a.create_image(350,350,image=t,state=HIDDEN)
    
#for a second angry face on double click
def angry_face2(event):
    angry_emoji_cuss=a.create_image(350,350,image=t,state=NORMAL)
    party_emoji=a.create_image(350,350,image=s,state=HIDDEN)
    sad_emoji=a.create_image(350,350,image=q,state=HIDDEN)
    angry_emoji=a.create_image(350,350,image=n,state=HIDDEN)
    happy_emoji=a.create_image(350,350,image=o,state=HIDDEN)
    blush_emoji=a.create_image(350,350,image=r,state=HIDDEN)


    
# to specify the role of each button wrt a function
a.bind('<Enter>',happy_face)
a.bind('<Leave>',sad_face)
a.bind('<Button-1>',angry_face1)
a.bind('<Button-2>',blush_face)
a.bind('<Button-3>',party_face)
a.bind('<Double-1>',angry_face2)
a.focus_set()
root.mainloop()
