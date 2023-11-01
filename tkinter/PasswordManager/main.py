from tkinter import*
from tkinter import messagebox
from random  import randint,shuffle,choice
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generatepassword():
    passentry.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_letters = [choice(letters) for _ in range(8,10)]
    pass_numbers = [choice(numbers) for _ in range(2,4)]
    pass_symbols = [choice(symbols) for _ in range(2,4)]
     
    password_list = pass_letters+pass_numbers+pass_symbols
    shuffle(password_list)
    password =  "".join(password_list)
    passentry.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = webentry.get()
    email = emailentry.get()
    password = passentry.get()
    new_data={
        website:{
            "email":email,
            "password":password
        }
    }

    if website=="" or password=="":
        messagebox.showinfo(title="Oops!!",message="Opps! \nplease the fill the requied detailes")
        
    else:
        try:    
            with open("data.json","r") as data_file:
            #reading the file
               data = json.load(data_file)
               
       
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data,data_file,indent=4)

        else:
            #updating data
            data.update(new_data)
            with open("data.json","w") as data_file:
               json.dump(data,data_file, indent=4)

        

    webentry.delete(0,END)
    passentry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def findpassword():
    website = webentry.get()
    try:
       with open("data.json","r") as data_file:
          data = json.load(data_file)

    except:
        messagebox.showinfo(title="Error",message="no data found")
        
    else:
        if website in data:
              email = data[website]["email"]
              password = data[website]["password"]
              messagebox.showinfo("Details",message=f"Email : {email}\nPassword : {password}")
        else:
            messagebox.showinfo(title="Error Message",message=f"{website} has no data")

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

#canvas
canvas = Canvas(width=200,height=200)
logo=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo) 
canvas.grid(column=1,row=0)


#labels
label1=Label(text="Website:",font=("classic",10))
label1.grid(column=0,row=1)


label2=Label(text="Email/Username:",font=("classic",10))
label2.grid(column=0,row=2)

label3=Label(text="Password:",font=("classic",10))
label3.grid(column=0,row=3)


#entries
webentry=Entry(width=22)
webentry.focus()
webentry.grid(column=1,row=1)


emailentry=Entry(width=43)
emailentry.insert(0,"puneeth@gmail.com")
emailentry.grid(column=1,row=2,columnspan=2)

passentry=Entry(width=22)
passentry.grid(column=1,row=3)

#buttons

passbutton=Button(text="Generate password",command=generatepassword)
passbutton.grid(column=2,row=3)

addbutton=Button(text="Add",width=35,command=save)
addbutton.grid(column=1,row=4,columnspan=2)

search_button = Button(text="Search",width=17,command=findpassword)
search_button.grid(column=2,row=1)





window.mainloop()
