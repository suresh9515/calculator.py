from tkinter import *
import tkinter.messagebox as tmsg
import os
import time
from math import * 

def getvals(event):
    value = event.widget.cget('text')
    if value=='Clr':
        sc_variable.set('')
    elif value=='=':
        try:
            sc_variable.set(eval(screen.get()))
            screen.update()
        except Exception as e:
            sc_variable.set('Error...')
            screen.update()
            status_var.set('Preparing...')
            screen.update()
            time.sleep(3)
            sc_variable.set('')
        
     
            screen.update()

    else:
        sc_variable.set(f'{sc_variable.get()}{value}')



def how_to_use():
    tmsg.showinfo('how to use','the trignometic functions should be used within the paranthesis')
def designed_by():
    tmsg.showinfo('designed by','hari suresh and siva nagireddy')

def send_feedback():
    ans=tmsg.askquestion('Feedback Hub','Was your experience good with us ? ')
    if ans=='yes':
        tmsg.showinfo('Feedback','THANK YOU RATE ON PLAYSTORE')
    else:
        tmsg.showinfo('Feedback','We will contact you soon to know about your bad experience')

root=Tk()
canvas_width=555
canvas_height=620
root.geometry(f'{canvas_width}x{canvas_height}')
root.maxsize(canvas_width,canvas_height)
root.minsize(canvas_width,canvas_height)
root.title('CalCulator ')




my_menu=Menu(root)
m1=Menu(my_menu,tearoff=0,fg='red')
m1.add_command(label='how to Use',command=how_to_use)
m1.add_command(label='Send Feedback',command=send_feedback)
m1.add_command(label='designed by',command=designed_by)
root.config(menu=my_menu)
my_menu.add_cascade(label=' About ',menu=m1)
my_menu.add_command(label='Exit',command=quit)


sc_variable=StringVar()
screen=Entry(root,textvariable=sc_variable,font='lucida 35 bold',fg='black',bg='white',borderwidth=10)
screen.pack(pady=30)


f=Frame(root)
f.pack()
b1=b2=Button(f,text='Clr',font='lucida 15 bold',padx=63,pady=20,borderwidth=3,fg='white',bg='red',width=3)

b3=Button(f,text='exp',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='white',bg='magenta',width=3)

b4=Button(f,text='sinh',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='white',bg='deepskyblue',width=3)

b5=Button(f,text='cosh',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='white',bg='deepskyblue',width=3)

b6=Button(f,text='tanh',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='white',bg='deepskyblue',width=3)


b1.bind('<Button-1>',getvals)
b2.bind('<Button-1>',getvals)
b3.bind('<Button-1>',getvals)
b4.bind('<Button-1>',getvals)
b5.bind('<Button-1>',getvals)
b6.bind('<Button-1>',getvals)
buttons=[b1,b2,b3,b4,b5,b6]
count=0
for i in range(6):
        buttons[count].grid(row=1,column=i)
        count += 1


f=Frame(root)
f.pack()
b1=Button(f,text='7',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='white',bg='black',width=3)

b2=Button(f,text='8',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='white',bg='black',width=3)

b3=Button(f,text='9',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='white',bg='black',width=3)

b4=Button(f,text='+',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='white',bg='magenta',width=3)

b5=Button(f,text='sin',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='white',bg='deepskyblue',width=3)

b6=Button(f,text='(',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='white',bg='magenta',width=3)


b1.bind('<Button-1>',getvals)
b2.bind('<Button-1>',getvals)
b3.bind('<Button-1>',getvals)
b4.bind('<Button-1>',getvals)
b5.bind('<Button-1>',getvals)
b6.bind('<Button-1>',getvals)
buttons=[b1,b2,b3,b4,b5,b6]
count=0
for i in range(6):
    buttons[count].grid(row=2,column=i)
    count += 1
f=Frame(root)
f.pack()
b1=Button(f,text='4',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='white',bg='black',width=3)

b2=Button(f,text='5',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='white',bg='black',width=3)

b3=Button(f,text='6',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='white',bg='black',width=3)

b4=Button(f,text='-',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='white',bg='magenta',width=3)

b5=Button(f,text='cos',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='white',bg='deepskyblue',width=3)

b6=Button(f,text=')',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='white',bg='magenta',width=3)


b1.bind('<Button-1>',getvals)
b2.bind('<Button-1>',getvals)
b3.bind('<Button-1>',getvals)
b4.bind('<Button-1>',getvals)
b5.bind('<Button-1>',getvals)
b6.bind('<Button-1>',getvals)
buttons=[b1,b2,b3,b4,b5,b6]
count=0
for i in range(6):
    buttons[count].grid(row=3,column=i)
    count += 1
f=Frame(root)
f.pack()
b1=Button(f,text='1',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='white',bg='black',width=3)

b2=Button(f,text='2',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='white',bg='black',width=3)

b3=Button(f,text='3',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='white',bg='black',width=3)

b4=Button(f,text='*',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='white',bg='magenta',width=3)

b5=Button(f,text='tan',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='white',bg='deepskyblue',width=3)

b6=Button(f,text='pi',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='white',bg='magenta',width=3)

b1.bind('<Button-1>',getvals)
b2.bind('<Button-1>',getvals)
b3.bind('<Button-1>',getvals)
b4.bind('<Button-1>',getvals)
b5.bind('<Button-1>',getvals)
b6.bind('<Button-1>',getvals)
buttons=[b1,b2,b3,b4,b5,b6]
count=0
for i in range(6):
    buttons[count].grid(row=4,column=i)
    count += 1
f=Frame(root)
f.pack()



b1=Button(f,text='.',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='white',bg='magenta',width=3)

b2=Button(f,text='0',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='white',bg='black',width=3)



b3=Button(f,text='%',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='white',bg='magenta',width=3)

b4=Button(f,text='/',font='lucida 15 bold',padx=20,pady=20,borderwidth=3,fg='white',bg='magenta',width=3)

b5=b6=Button(f,text='=',font='lucida 15 bold',padx=63,pady=20,borderwidth=3,fg='white',bg='#00ff00',width=3)


b1.bind('<Button-1>',getvals)
b2.bind('<Button-1>',getvals)
b3.bind('<Button-1>',getvals)
b4.bind('<Button-1>',getvals)
b5.bind('<Button-1>',getvals)
b6.bind('<Button-1>',getvals)
buttons=[b1,b2,b3,b4,b5,b6]
count=0
for i in range(6):
    buttons[count].grid(row=5,column=i)
    count += 1

root.mainloop()
