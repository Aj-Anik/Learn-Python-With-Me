#Functions & Recursion in Python

#Functions: To easily repeat code 
#How to write function
# def func_name (param 1 , param 2 ......):
# some works 
# return value
#here we wrote def it means function definition



def sum (a , b):
    c = a + b 
    print(c)


sum (3 , 5)
sum (4 , 6)
sum (13, 7)


def say_hello():
    print("hello guys")

say_hello()



#Python has 2 types of functions 1. built in functions  2. user defined functions

# 1. Built in functions : print() ,  len() , type() , range()

# 2. user defined functions :


#make a function of a factorial 
def fact(n):
    result = 1
    for i in range(1 , n+1) :
        result *= i
    print (result)

fact(5)



# wap which can detect even & odd numbers
p = int(input("Enter the number : "))
print(p)
if(p%2==0):
    print("EVEN", end = "\n")
else:
    print("ODD",end="\n")


# if we want to print two line without next line we can write like this 

print("welcome to")
print("Bangladesh")

#here two of the lines are in separate lines but we can write like this 

print("welcome to" , end = " ")  # we have switch the \n into a space
print("Bangladesh")  #there we can pass anything which will be replace with the end = " " we can even pass a $ sign 



#######################################



# Recursion : self calling function , loops are recursion are brothers

def show(n):
    print(n)

show(5)  # this is a simple code but if we want to print the 5 4 3 2 ....we have to use recursion

def seen(n):
    if(n==0): return     # here is the base case of our recursion
    print(n , end=" ") 
    seen(n-1)

seen(10)

# Factorial using recursion :
def fact(n):
    if(n == 1 or n == 0): return 1
    else :
        return n * fact(n-1)
    
print(fact(5))