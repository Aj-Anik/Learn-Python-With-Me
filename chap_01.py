print("hello world")


name = "anik" #string
age = 22 # int
uni = "IIUC" # string
price = 24.99 # decimal
gender_male = True  # to use bool we have to write True , False
null = None # Another type of variable called None type

print(name)
print(age)
print(uni)
print(gender_male)
print(null)

a = 6  # '=' is called assignment operation
b = 5
print(a+b)

c = b
d = a
print(c*d)

#how to check type of variables :
print(type(name))
print(type(age))
print(type(price))
print(type(gender_male))
print(type(null))

#python is a case sensitive language

#Comments in Python

# Single Line comments
"""
This is Multi Line Comments 
"""

#Arithmatics Op
# +  -  *  /  %  **
# here ** is a new Operation  which is use like this if a = 2 ** 4   it means 2 * 2 * 2 * 2  (2^4)


#Relational Op
# ==  <=  >=  < > !=

#Assignment Op
# += -= *= = /= **= %=

#Logical Op
# && and , || or  , ! not





#  1. Type Conversion(Auto)    2. Type Casting(Manual)


# Type Conversion
X = 5
Y = 2.5
sum2 = X + Y
print(sum2)   # as float is a superior that why the int value becomes float


#Type Casting
A = "5"
B = 7
# print(A+B) #It will be wrong as we cant add a int with a string

A2 = int("3") # here we did a type casting

print(A2+B)


#Using Input    input()
NAME = input("Enter Your name : ")

print(type(NAME))


#for input int / float

aGe = int(input("Enter Your AGE : "))
print(type(aGe))

#If Else system
# after giving a statement in If & else or else if we have to use ':'

a_1 = 5
b_1 = 3

if(a_1 > b_1):
    print("a is greater than b")
else:
    print("a is less than b")






#Practice Problem:
#1. Input 2 value & output their sum

P =int(input("Enter the first value : "))
Q = int(input("Enter the second value : "))
print(P+Q)

#2. Output the area of a Square
L = float(input("Enter the one side of a Square : "))
area = L ** 2
print(area )

#3. if a > b then print True otherwise print False
Aa = 5
Bb = 3
if(Aa>Bb):
    print(True)
else: print(False)