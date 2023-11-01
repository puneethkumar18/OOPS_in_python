from tkinter import * 

Window=Tk()
Window.title("Graphical User Interface")
Window.minsize(width=400,height=200)

#lable
l_lable=Label(text="My Name",font=("classic",20,"bold"))
l_lable.pack(side="top")




def gotclicked():
    new=input.get()
    l_lable["text"]=new

#Botton
button=Button(text="click me",command=gotclicked)
button.pack()

#entry
input=Entry(width=10)
input.pack()


#check button
def check_state():
    print(new_state.get())

new_state=IntVar()
check=Checkbutton(text="is it on",variable=new_state,command=check_state)
check.pack()





Window.mainloop()