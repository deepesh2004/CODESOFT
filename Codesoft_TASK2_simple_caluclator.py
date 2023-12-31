#TASK 2
#creating a simple caluclator
from tkinter import *
root=Tk()
root.title('caluclator')
e=Entry(root,width=40,borderwidth=20)
e.grid(row=0,column=0,columnspan=3)
def button_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
    return
def button_clear():
    e.delete(0,END)
def button_add():
    first_number=e.get()
    global f_num
    global math
    math='addition'
    f_num=int(first_number)
    e.delete(0,END)
def button_sub():
    first_number=e.get()
    global f_num
    global math
    math='subraction'
    f_num=int(first_number)
    e.delete(0,END)
def button_div():
    first_number=e.get()
    global f_num
    global math
    math='division'
    f_num=int(first_number)
    e.delete(0,END)
def button_mul():
    first_number=e.get()
    global f_num
    global math
    math='multiplication'
    f_num=int(first_number)
    e.delete(0,END)
def button_equal():
    second_number=e.get()
    e.delete(0,END)
    if math=='addition':
        e.insert(0,f_num+int(second_number))
    elif math=='subraction':
        e.insert(0,f_num-int(second_number))
    elif math=='division':
        e.insert(0,f_num/int(second_number))
    elif math=='multiplication':
        e.insert(0,f_num*int(second_number))
button_0=Button(root,text='clear',padx=120,pady=20,command=button_clear).grid(row=6,column=0,columnspan=3)
button_1=Button(root,text='1',padx=40,pady=20,command=lambda:button_click(1)).grid(row=1,column=0)
button_2=Button(root,text='2',padx=40,pady=20,command=lambda:button_click(2)).grid(row=1,column=1)
button_3=Button(root,text='3',padx=40,pady=20,command=lambda:button_click(3)).grid(row=1,column=2)
button_4=Button(root,text='4',padx=40,pady=20,command=lambda:button_click(4)).grid(row=2,column=0)
button_5=Button(root,text='5',padx=40,pady=20,command=lambda:button_click(5)).grid(row=2,column=1)
button_6=Button(root,text='6',padx=40,pady=20,command=lambda:button_click(6)).grid(row=2,column=2)
button_7=Button(root,text='7',padx=40,pady=20,command=lambda:button_click(7)).grid(row=3,column=0)
button_8=Button(root,text='8',padx=40,pady=20,command=lambda:button_click(8)).grid(row=3,column=1)
button_9=Button(root,text='9',padx=40,pady=20,command=lambda:button_click(9)).grid(row=3,column=2)
button_10=Button(root,text='0',padx=40,pady=20,command=lambda:button_click(0)).grid(row=4,column=0)
button_11=Button(root,text='+',padx=40,pady=20,command=button_add).grid(row=4,column=1)
button_12=Button(root,text='=',padx=40,pady=20,command=button_equal).grid(row=4,column=2)
button_13=Button(root,text='-',padx=40,pady=20,command=button_sub).grid(row=5,column=0)
button_14=Button(root,text='/',padx=40,pady=20,command=button_div).grid(row=5,column=1)
button_15=Button(root,text='*',padx=40,pady=20,command=button_mul).grid(row=5,column=2)
root.mainloop()