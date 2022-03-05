from tkinter import*
from tkinter import font
root=Tk()
root.title("CODER")
root.config(bg="green")
global str_
#CREATING BUTTON FUNCTION 
def add(a):
    ent.insert(END,a)

    pass
def equal():
    temp=eval(ent.get())
    ent.delete(0,END)
    if(temp==317):
        label=Label(root,text="CODER BIRTHDAY DAY YOU GOT IN THE ENTRY MENU",bg="blue",fg="black",font=(("Helvetica", "16")))
        label.pack()
    ent.insert(0,temp)
    button_temp.config(text=temp)
def clear():
    temp=ent.get()
    temp=len(temp)-1
    ent.delete(temp)

#CREATING LABEL FOR CODER CALCULATOR
label=Label(root,text='CODER CALCULATOR',padx=300,pady=30,fg='cyan',bg='black',font=('Helvetica bold',40))

#PACKINT LABEL
label.place(x=200,y=20)
#CREATING ENTRY WIDGET
var_ent=StringVar()
ent=Entry(root,bd=10,font=(('Verdana',50)),textvariable=var_ent)
ent.place(x=300,y=150)
#MAKING TEXT VARIABLE
var1=StringVar(value='1')
var2=StringVar(value='2')
var3=StringVar(value='3')
var4=StringVar(value="4")
var5=StringVar(value='5')
var6=StringVar(value='6')
var7=StringVar(value='7')
var8=StringVar(value='8')
var9=StringVar(value='9')
var0=StringVar(value='0')

#MAKING BUTTONS 
button_1=Button(root,text=var1,bd=4,padx=40,pady=10,width=10,relief=RIDGE,height=5,activebackground="cyan",activeforeground="black",fg='black',bg='#889eb9',command=lambda:add("1"),textvariable=var1)
button_2=Button(root,text=var2,bd=4,padx=40,pady=10,width=10,relief=RIDGE,height=5,activebackground="cyan",activeforeground="black",font=('Helvetica bold',10),fg='black',bg='#889eb9',command=lambda:add("2"),textvariable=var2)
button_3=Button(root,text=var3,bd=4,padx=40,pady=10,width=10,relief=RIDGE,height=5,activebackground="cyan",activeforeground="black",fg='black',bg='#889eb9',command=lambda:add("3"),textvariable=var3)
button_4=Button(root,text=var3,bd=4,padx=40,pady=10,width=10,relief=RIDGE,height=5,activebackground="cyan",activeforeground="black",fg='black',bg='#889eb9',command=lambda:add("4"),textvariable=var4)
button_5=Button(root,text=var4,bd=4,padx=40,pady=10,width=10,relief=RIDGE,height=5,activebackground="cyan",activeforeground="black",fg='black',bg='#889eb9',command=lambda:add("5"),textvariable=var5)
button_6=Button(root,text=var6,bd=4,padx=40,pady=10,width=10,relief=RIDGE,height=5,activebackground="cyan",activeforeground="black",fg='black',bg='#889eb9',command=lambda:add("6"),textvariable=var6)
button_7=Button(root,text=var7,bd=4,padx=40,pady=10,width=10,relief=RIDGE,height=5,activebackground="cyan",activeforeground="black",fg='black',bg='#889eb9',command=lambda:add("7"),textvariable=var7)
button_8=Button(root,text=var8,bd=4,padx=40,pady=10,width=10,relief=RIDGE,height=5,activebackground="cyan",activeforeground="black",fg='black',bg='#889eb9',command=lambda:add("8"),textvariable=var8)
button_9=Button(root,text=var9,bd=4,padx=40,pady=10,width=10,relief=RIDGE,height=5,activebackground="cyan",activeforeground="black",fg='black',bg='#889eb9',command=lambda:add("9"),textvariable=var9)
button_0=Button(root,text=var0,bd=4,padx=40,pady=10,width=10,relief=RIDGE,height=5,activebackground="cyan",activeforeground="black",fg='black',bg='#889eb9',command=lambda:add("0"),textvariable=var0)
button_temp=Button(root,text="HISTORY",bd=4,padx=40,pady=10,width=10,relief=RIDGE,height=5,activebackground="cyan",activeforeground="black",fg='white',bg='black')
button_plus=Button(root,text='+',bd=4,padx=40,pady=10,width=10,relief=RIDGE,height=5,activebackground="cyan",activeforeground="black",fg='black',bg='#889eb9',command=lambda:add("+"),)
button_minus=Button(root,text='--',bd=4,padx=40,pady=10,width=10,relief=RIDGE,height=5,activebackground="cyan",activeforeground="black",fg='black',bg='#889eb9',command=lambda:add("-"))
button_div=Button(root,text='/',bd=4,padx=40,pady=10,width=10,relief=RIDGE,height=5,activebackground="cyan",activeforeground="black",fg='black',bg='#889eb9',command=lambda:add("/"))
button_multliplication=Button(root,text='*',bd=4,padx=40,pady=10,width=10,relief=RIDGE,height=5,activebackground="cyan",activeforeground="black",fg='GREEN',bg='#889eb9',command=lambda:add("*"))
button_equal=Button(root,text='=',bd=4,padx=40,pady=15,width=10,relief=RIDGE,height=5,activebackground="cyan",activeforeground="black",fg='black',bg='#889eb9',command=equal)
button_=Button(root,text='CLEAR',bd=4,padx=40,pady=70,width=10,relief=RIDGE,height=5,activebackground="cyan",activeforeground="black",fg='black',bg='#889eb9',command=clear)
click=Button(root,text="click me",bd=20)
#PLACING BUTTONS 
click.place(relx=0.3,y=0.3)
click.place(x=100,y=800)
button_1.place(x=300,y=530)
button_2.place(x=500,y=530)
button_3.place(x=700,y=530)
button_4.place(x=300,y=400)
button_5.place(x=500,y=400)
button_6.place(x=700,y=400)
button_7.place(x=300,y=270)
button_8.place(x=500,y=270)
button_9.place(x=700,y=270)
button_0.place(x=500,y=650)
button_temp.place(x=300,y=650)
button_equal.place(x=700,y=650)
button_plus.place(x=870,y=270)
button_minus.place(x=870,y=400)
button_div.place(x=870,y=530)
button_multliplication.place(x=870,y=650)
button_.place(x=1050,y=270)

root.mainloop()
