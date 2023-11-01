from tkinter import *

window = Tk()
window.minsize(width=200,height=140)
window.title("Km to mile Converter")
window.config(padx=30,pady=30)

#entry
entry=Entry(width=8)
entry.grid(column=1,row=0)

#lable
lable = Label(text="miles",font=("classic",10,"bold"))
lable.grid(column=2,row=0)

lable1 = Label(text="is equal to",font=("classic",10,"bold"))
lable1.grid(column=0,row=1)

lable2 = Label(text="0",font=("classic",10,"bold"))  
lable2.grid(column=1,row=1)

lable3 = Label(text="kms",font=("classic",10,"bold"))
lable3.grid(column=2,row=1)

#Button 
def clicked():
    result= float(entry.get())
    answer= round(result*1.7)
    lable2.config(text= answer)

button=Button(text="Calculate",command=clicked)
button.grid(column=1,row=2)



window.mainloop()