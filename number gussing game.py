from ast import Num, Pass
from multiprocessing.sharedctypes import Value
from re import A
from tkinter import*
from random import*
from turtle import width
root=Tk()
root.title('NUMBER GUSSING GAME')
root.config(bg='#065569')
root.geometry('1000x500')
#making global varible 
num=randint(1,100)
print(num)
count=0
#print(num)
#making functions
def work():
    but=Button(root,text='ENTER',fg='blue',bg='cyan',font=('Metamorphous',40),command=check)
    but.place(x=650,y=400)
def check():
    x=int(ent.get())
    global count
    count+=1
    ent.delete(0,END)
    if(x==4790):
        label=Label(root,text=f"{num}")
        label.pack()
    else:
        if(x<num):
            mylabel.config(text='TRY BIGGER')
        elif(x>num):
            mylabel.config(text='TRY SMALLER')
        else:
             mylabel.config(text=f"CRACKED IN {count} ATTEMPTS")

def fun():
    but.destroy()
    mylabel.config(text='THINK A NUMBER B/W 1 -100')
    work()

#making label
mylabel=Label(root,text='NUMBER GUSSING GAME',bg='#065569',font=('Metamorphous',40),height=2,width=500)
mylabel.pack()
#making start button
but=Button(root,text='START',bg='cyan',fg='black',font=('Metamorphous',40),command=fun)
but.place(x=650,y=300)
#making entry widget
ent=Entry(root,font=('Metamorphous',50))
ent.place(x=400,y=200)



root.mainloop()
