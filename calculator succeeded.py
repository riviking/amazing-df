#####++++calculator for addition only++++#####

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
    
        
        

list=[]
def but_plus():
    #plus
    current=e.get()
    e.delete(0,END)
    list.append(int(current))
    global summ
    summ=sum(list)
    

def but_eq():
    # equal
    current=e.get()
    e.delete(0,END)
    
    final=summ+int(current)
    e.insert(0,final)
    #print("summ:",summ,"final:",final,"list:",list)
    list.clear()

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

root.mainloop()
