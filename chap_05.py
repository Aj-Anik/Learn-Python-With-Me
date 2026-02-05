#Loops in Python
i = 1
while i<5 :
    print("Hello World")
    i += 1


#multiplication table of a number n
num = 3
i = 1
while i<=10:
    print(num*i)
    i += 1

#print the element of a list
nums = [1 , 2 , 4 , 9 , 13 , 14 , 18  , 61 , 84 , 100]
i = 0
x = len(nums)

while(i < x) :
    print(nums[i])
    i+=1



#search an element from a tuple 
tup = (1 , 2 , 4 , 9 , 13 , 14 , 18  , 61 , 84 , 100)

p = int(input("enter the value you want to find : "))
xx = len(tup)
ii = 0
check = False

while ii < xx :
    if(tup[ii] == p):
        check = True
        print("Found\n")
        break 
    else:
        ii+=1
    
if(check == False):
    print("Not Found\n")



#break & Continue



#For Loop 
 
num = [1 , 2 , 3 , 4 , 5 ]
i = 0
for val in num :
    print(val)
    i+=1


str = "Aj Anik"

for char in str :
    print(char)

# we can also use else in for loop 


#range function 

print(range(5))


seq = range(5)
for i in seq :
    print(i)


seq1 = range(4 , 10)   # it means range(start , end)

seq2 = range(3 , 15 , 3)  #it means range (start , end , step ) step means i+=3

#if we want to print all the even numbers from 1 to 100
seq0 = range(2 , 100 , 2)
for i in seq0:
    print(i)



#pass statement
#if we want a statement empty we use pass
for i in range(5):
    pass     # we use pass no work in the loop or we want to work there for future

