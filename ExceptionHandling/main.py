try:
    file=open("data.txt")
    list=[1,2,3,4]
    print(list[3])

except FileNotFoundError:
    file=open("data.txt","w")
    file.write("puneeth kumar")

#except block run if try block gives an Error 
except IndexError as error_index:
    print(f"{error_index} is not available")

#else block runs while try won't give any error
else:
    print(file.read())
#finally runs without dependent action of try block
finally:
    file.close()
    print("file is closed")

#raise Error
height=int(input("Height:"))

if height>10:
    raise ValueError("this not possble")