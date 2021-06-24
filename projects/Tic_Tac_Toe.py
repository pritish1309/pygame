from tkinter import*
from tkinter import messagebox
p=Tk()
p.title("Tic Tac Toe ")

# X starts first in true state
clicks=True
turn=0

# function to disable all buttons after thebgame finishes

def disable_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)



# creating a function to check who won

def check_win():
    global winner
    winner=False

    # cases for X winning
    
    if b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS !\nX wins")
        disable_buttons()

    elif b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner = True        
        messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS !\nX wins")
        disable_buttons()

    elif b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner = True 
        messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS !\nX wins")
        disable_buttons()

    elif b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner = True        
        messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS !\nX wins")
        disable_buttons()

    elif b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner = True  
        messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS !\nX wins")
        disable_buttons()

    elif b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner = True 
        messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS !\nX wins")
        disable_buttons()

    elif b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner = True 
        messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS !\nX wins")
        disable_buttons()

    elif b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner = True 
        messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS !\nX wins")
        disable_buttons()
    
    # cases for O winning
    
    if b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner = True 
        messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS !\n0 wins")
        disable_buttons()

    elif b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS !\n0 wins")
        disable_buttons()

    elif b7["text"]=="O" and b8["text"]=="O" and b9["text"]=="O":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner = True 
        messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS !\n0 wins")
        disable_buttons()

    elif b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner = True 
        messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS !\n0 wins")
        disable_buttons()

    elif b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner = True 
        messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS !\n0 wins")
        disable_buttons()

    elif b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner = True 
        messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS !\n0 wins")
        disable_buttons()

    elif b1["text"]=="O" and b5["text"]=="O" and b9["text"]=="O":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS !\n0 wins")
        disable_buttons()

    elif b3["text"]=="O" and b5["text"]=="O" and b7["text"]=="O":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe","CONGRATULATIONS !\n0 wins")
        disable_buttons()

    elif turn==9 and winner==False:
        messagebox.showerror("Tic Tac Toe","It's a tie !\nNo one wins")
        disable_buttons()







# clicking button function

def click_button(b):
    global clicks, turn

    if b["text"]==" " and clicks==True :
        b["text"] = "X"
        clicks=False
        turn+=1
        check_win()
    
    elif b["text"]==" " and clicks==False :
        b["text"] = "O"
        clicks=True
        turn+=1
        check_win()

    else :
        messagebox.showerror("Tic Tac Toe","This block is already occupied\nPlease selt another box !")



# to reset the game
def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global turn, clicks
    clicks=True
    turn=0

    # Butttons

    b1=Button(p,text=" ",font="20",height=4,width=6,bg="SystemButtonFace",command=lambda: click_button(b1))
    b2=Button(p,text=" ",font="20",height=4,width=6,bg="SystemButtonFace",command=lambda: click_button(b2))
    b3=Button(p,text=" ",font="20",height=4,width=6,bg="SystemButtonFace",command=lambda: click_button(b3))

    b4=Button(p,text=" ",font="20",height=4,width=6,bg="SystemButtonFace",command=lambda: click_button(b4))
    b5=Button(p,text=" ",font="20",height=4,width=6,bg="SystemButtonFace",command=lambda: click_button(b5))
    b6=Button(p,text=" ",font="20",height=4,width=6,bg="SystemButtonFace",command=lambda: click_button(b6))

    b7=Button(p,text=" ",font="20",height=4,width=6,bg="SystemButtonFace",command=lambda: click_button(b7))
    b8=Button(p,text=" ",font="20",height=4,width=6,bg="SystemButtonFace",command=lambda: click_button(b8))
    b9=Button(p,text=" ",font="20",height=4,width=6,bg="SystemButtonFace",command=lambda: click_button(b9))

    # positioning buttons
    b1.grid(row=0,column=0)
    b2.grid(row=0,column=1)
    b3.grid(row=0,column=2)

    b4.grid(row=1,column=0)
    b5.grid(row=1,column=1)
    b6.grid(row=1,column=2)

    b7.grid(row=2,column=0)
    b8.grid(row=2,column=1)
    b9.grid(row=2,column=2)


# creating a menu with reset button
reset_menu=Menu(p)
p.config(menu=reset_menu)

options_menu = Menu(reset_menu)
reset_menu.add_cascade(label="Options",menu=options_menu)
options_menu.add_command(label="Reset",command=reset)

reset()
p.mainloop()
