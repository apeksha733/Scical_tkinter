from tkinter import *
import tkinter.messagebox as tmsg

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
            sc_variable.set('Error')
            screen.update()
           

    else:
        sc_variable.set(f'{sc_variable.get()}{value}')



root=Tk()
width=555
height=620
root.geometry(f'555x620')
root.maxsize(width,height)
root.minsize(width,height)
root.title('Scientific Calculator ')


sc_variable=StringVar()
screen=Entry(root,textvariable=sc_variable,font='calibri 35 bold',fg='black',bg='light grey',borderwidth=10)
screen.pack(pady=30)


f=Frame(root)
f.pack()

b1=Button(f,text='1',font='calibri 15 bold',padx=20,pady=10,borderwidth=3,fg='white',bg='darkblue',width=3)

b2=Button(f,text='2',font='calibri 15 bold',padx=20,pady=10,borderwidth=3,fg='white',bg='darkblue',width=3)

b3=Button(f,text='3',font='calibri 15 bold',padx=20,pady=10,borderwidth=3,fg='white',bg='darkblue',width=3)

b4=Button(f,text='*',font='calibri 15 bold',padx=20,pady=10,borderwidth=3,fg='white',bg='black',width=3)

b5=Button(f,text='(',font='calibri 15 bold',padx=20,pady=10,borderwidth=3,fg='white',bg='black',width=3)

b6=Button(f,text='log10',font='calibri 15 bold',padx=20,pady=10,borderwidth=3,fg='white',bg='black',width=3)

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
b1=Button(f,text='4',font='calibri 15 bold',padx=20,pady=10,borderwidth=3,fg='white',bg='darkblue',width=3)

b2=Button(f,text='5',font='calibri 15 bold',padx=20,pady=10,borderwidth=3,fg='white',bg='darkblue',width=3)

b3=Button(f,text='6',font='calibri 15 bold',padx=20,pady=10,borderwidth=3,fg='white',bg='darkblue',width=3)

b4=Button(f,text='-',font='calibri 15 bold',padx=20,pady=10,borderwidth=3,fg='white',bg='black',width=3)

b5=Button(f,text=')',font='calibri 15 bold',padx=20,pady=10,borderwidth=3,fg='white',bg='black',width=3)

b6=Button(f,text='log',font='calibri 15 bold',padx=20,pady=10,borderwidth=3,fg='white',bg='black',width=3)


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


b1=Button(f,text='7',font='calibri 15 bold',padx=20,pady=10,borderwidth=3,fg='white',bg='darkblue',width=3)

b2=Button(f,text='8',font='calibri 15 bold',padx=20,pady=10,borderwidth=3,fg='white',bg='darkblue',width=3)

b3=Button(f,text='9',font='calibri 15 bold',padx=20,pady=10,borderwidth=3,fg='white',bg='darkblue',width=3)

b4=Button(f,text='+',font='calibri 15 bold',padx=20,pady=10,borderwidth=3,fg='white',bg='black',width=3)

b5=Button(f,text='%',font='calibri 15 bold',padx=20,pady=10,borderwidth=3,fg='white',bg='black',width=3)

b6=Button(f,text='hypot',font='calibri 15 bold',padx=20,pady=10,borderwidth=3,fg='white',bg='black',width=3)


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



f=Frame(root)
f.pack()
b1=Button(f,text='e',font='calibri 15 bold',padx=20,pady=10,borderwidth=3,fg='white',bg='black',width=3)

b2=Button(f,text='0',font='calibri 15 bold',padx=20,pady=10,borderwidth=3,fg='white',bg='darkblue',width=3)

b3=Button(f,text='pi',font='calibri 15 bold',padx=20,pady=10,borderwidth=3,fg='white',bg='black',width=3)

b4=Button(f,text='/',font='calibri 15 bold',padx=20,pady=10,borderwidth=3,fg='white',bg='black',width=3)

b5=Button(f,text='.',font='calibri 15 bold',padx=20,pady=10,borderwidth=3,fg='white',bg='black',width=3)

b6=Button(f,text=',',font='calibri 15 bold',padx=20,pady=10,borderwidth=3,fg='white',bg='black',width=3)


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



b1=Button(f,text='sin',font='calibri 15 bold',padx=20,pady=10,borderwidth=3,fg='white',bg='black',width=3)

b2=Button(f,text='cos',font='calibri 15 bold',padx=20,pady=10,borderwidth=3,fg='white',bg='black',width=3)

b3=Button(f,text='tan',font='calibri 15 bold',padx=20,pady=10,borderwidth=3,fg='white',bg='black',width=3)

b4=Button(f,text='asin',font='calibri 15 bold',padx=20,pady=10,borderwidth=3,fg='white',bg='black',width=3)

b5=Button(f,text='acos',font='calibri 15 bold',padx=20,pady=10,borderwidth=3,fg='white',bg='black',width=3)

b6=Button(f,text='atan',font='calibri 15 bold',padx=20,pady=10,borderwidth=3,fg='white',bg='black',width=3)

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


b1=Button(f,text='exp',font='calibri 15 bold',padx=20,pady=10,borderwidth=3,fg='white',bg='black',width=3)

b2=Button(f,text='tanh',font='calibri 15 bold',padx=20,pady=10,borderwidth=3,fg='white',bg='black',width=3)

b3=Button(f,text='sinh',font='calibri 15 bold',padx=20,pady=10,borderwidth=3,fg='white',bg='black',width=3)

b4=Button(f,text='cosh',font='calibri 15 bold',padx=20,pady=10,borderwidth=3,fg='white',bg='black',width=3)

b5=Button(f,text='gcd',font='calibri 15 bold',padx=20,pady=10,borderwidth=3,fg='white',bg='black',width=3)

b6=Button(f,text='=',font='calibri 15 bold',padx=20,pady=10,borderwidth=3,fg='white',bg='green',width=3)

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


b1=Button(f,text='pow',font='calibri 15 bold',padx=20,pady=10,borderwidth=3,fg='white',bg='black',width=3)

b2=Button(f,text='degrees',font='calibri 15 bold',padx=20,pady=10,borderwidth=3,fg='white',bg='black',width=3)

b3=Button(f,text='radians',font='calibri 15 bold',padx=20,pady=10,borderwidth=3,fg='white',bg='black',width=3)

b4=Button(f,text='sqrt',font='calibri 15 bold',padx=20,pady=10,borderwidth=3,fg='white',bg='black',width=3)

b5=Button(f,text='factorial',font='calibri 15 bold',padx=20,pady=10,borderwidth=3,fg='white',bg='black',width=3)

b6=Button(f,text='Clr',font='calibri 15 bold',padx=20,pady=10,borderwidth=3,fg='white',bg='red',width=3)


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
status_var=StringVar()

root.mainloop()
