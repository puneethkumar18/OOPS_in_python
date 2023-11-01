
import datetime as dt
import pandas
from random import randint
import smtplib

data = pandas.read_csv("birthdays.csv")
birthdays = {(row.day,row.month):row for (key,row) in data.iterrows()}

today = dt.datetime.now()
today = (today.day,today.month)
email = "puneethkumarg9@gmail.com"
password = "Dcet@2022"
if today in birthdays:
    current_row = birthdays[today]
    with open(f"letter_templates\letter_{randint(1,4)}.txt") as text_template:
        contents = text_template.read()
        contents = contents.replace("[NAME]",current_row.Name)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = email,password=password)
        connection.sendmail(from_addr=email,to_addrs=current_row.email,msg = f"Subject : Happy Birthday!!\n{contents}")
           
    
    




# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




