from tkinter import *


window = Tk()

def km_to_miles():
    print(e1_value.get())
    miles=float(e1_value.get())*1.6 # float to caculate wit number
    t1.insert(END,miles) # inset object such as text

b1=Button(window,text="Execute",command=km_to_miles) # name of data input
b1.grid(row=0,column=0)


e1_value=StringVar() # to call the corresponding constructor
e1=Entry(window,textvariable=e1_value) # to entry the data
e1.grid(row=0,column=1)

t1=Text(window,height=1,width=20) # size of data
t1.grid(row=0,column=2)

window.mainloop()
