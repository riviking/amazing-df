#####++++SUCCEED++++#####

from tkinter import *
root=Tk()
root.title("calculator")



e= Entry(root,width=50,borderwidth=5)
e.grid(row=0,column=0, columnspan=4)

def but_add(number):
    #type numbers
    if e.get()=="":
        e.insert(0,number)
    else:    
        current=e.get()
        e.delete(0,END)
        e.insert(0,current+str(number))

def but_clear():
    #clear
    e.delete(0,END)
    
        
        


def but_plus():
    #plus
    current=e.get()
    e.delete(0,END)
    global f_num
    global math  
    math="addition"
    f_num= int(current)
    
def but_sub():
    #substract
    current=e.get()
    e.delete(0,END)
    global f_num
    global math  
    math="substraction"
    f_num= int(current)    

def but_mult():
    #multiply
    current=e.get()
    e.delete(0,END)
    global f_num
    global math  
    math="multiply"
    f_num=int(current)

def but_div():
    #divide
    current=e.get()
    e.delete(0,END)
    global f_num
    global math  
    math="division"
    f_num= int(current)

def but_eq():
    current=e.get()
    e.delete(0,END)
    
    s_num=int(current)
    if math=="addition":
        e.insert(0, f_num+s_num)
    if math=="substraction":
        e.insert(0, f_num-s_num)
    if math=="multiply":
        e.insert(0, f_num*s_num)
        print(f_num,s_num,f_num*s_num)
    if math=="division":
        e.insert(0, f_num/s_num)
    #bug fixing
        

#calculator buttons
button_1=Button(root,text='1',padx=30,pady=30, command=lambda:but_add(1))
button_2=Button(root,text='2',padx=30,pady=30,command=lambda:but_add(2))
button_3=Button(root,text='3',padx=30,pady=30,command=lambda:but_add(3))
button_4=Button(root,text='4',padx=30,pady=30,command=lambda:but_add(4))
button_5=Button(root,text='5',padx=30,pady=30,command=lambda:but_add(5))
button_6=Button(root,text='6',padx=30,pady=30,command=lambda:but_add(6))
button_7=Button(root,text='7',padx=30,pady=30,command=lambda:but_add(7))
button_8=Button(root,text='8',padx=30,pady=30,command=lambda:but_add(8))
button_9=Button(root,text='9',padx=30,pady=30,command=lambda:but_add(9))
button_0=Button(root,text='0',padx=30,pady=30,command=lambda:but_add(0))
button_pl=Button(root,text='+',padx=30,pady=30, command=but_plus)
button_cl=Button(root,text='clear',padx=31,pady=116, command=but_clear)
button_eq=Button(root,text='=',padx=80,pady=30, command=but_eq)

button_sub=Button(root,text='-',padx=30,pady=30, command=but_sub)
button_mult=Button(root,text='x',padx=30,pady=30, command=but_mult)
button_div=Button(root,text='/',padx=30,pady=30, command=but_div)

#placing buttons
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_0.grid(row=4,column=1)
button_pl.grid(row=4,column=0)
button_cl.grid(row=1,column=3,rowspan=3)
button_eq.grid(row=4,column=2,columnspan=2)

button_sub.grid(row=5,column=0)
button_mult.grid(row=5,column=1)
button_div.grid(row=5,column=2)


root.mainloop()
