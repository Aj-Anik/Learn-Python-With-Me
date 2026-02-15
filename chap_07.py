# File I/O(input and output) in Python
# Python can be used to perform op. on a file (read & write data)

# before read or write , we have to open a file
# f = open("file name", "mode")    r = read mode , w = write mode
# then we have to use f.close()


# lets assume we have created a file name demo.txt

f = open("demo.txt" , "r")
data = f.read()
print(type(data))     #class will be as string 
f.close()

# some modes about file io
# r = to read a file   , w = to write a file   , x = creates a new file & open it for writing
# a = appending  , b = binary mode , t = text mode(default) , + = open a disk file for read & write


# if we hand to read the specific string we can write this 

data = f.read(5)
#this will print the 5 string from the txt file 



data = f.readline()
#this will read one line at a time 


# now we are using w mode

f = open("demo.txt", "w")
f.write("this is a new line") # overwrites the entire file cause we didnt use "a"
f.close()


# if we use a mode
f = open("demo.txt", "a")
f.write("this is an another new line") # the string will be add in a new line


# if we want to overwrite the text & make the new text in front we have to use r+ mode
# there is also w+ & a+


# now we can use with syntax
"""
with open("demo.txt", "a") as f:    
        data = f.read()
"""

with open("demo.txt","a") as f: # we can write anything we want just like as f 
    data = f.read()

    # when we use with syntax , we dont have to use close()

with open("demo.txt" , "w") as f:
    f.write("hello world")


# Deleting a File 
# here we cant delete a file only by using remove we need to use modules (module is like a code library which also have different functions)

import os 
    
os.remove("demo.txt")




