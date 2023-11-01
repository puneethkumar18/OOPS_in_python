


#another way to open file with no need of closing
with open("my_file.txt", "r") as file:
    content=file.read()
    print(content)

with open("my_file.txt", "a") as file:
    file.write("\nmy father police man ")

file = open("my_file.txt","r")
# mode is action doing with our file "r" to read by default is in read mode,"a" append to a file,"w"is to write in file
contents=file.read()
print(contents)
file.close()
    

with open("my_file.txt", "w") as file:
    content=file.write("my name is puneeth")
    print(content)

