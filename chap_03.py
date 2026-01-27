#List & Tuple in Python

#List is like arrays which stores various values
# LIST can store int , float , string ,

marks = [45 , 46 , 50 , 32 , 36]
print(marks)
print(type(marks))    #its type is list

#we can also access the list like this

print(marks[0])
print(len(marks))

# In python , String are immutable but list are mutable --> Mutable means we can change its value
"""str = "anik"
str[0] = "p"
print(str)"""
#here it cannot change



marks[0] = 50
print(marks[0])
print(marks)
#here we can change the value of my list


#Functions of List:

list = [2, 4, 1, 3, 7, 5, 8]
print(type(list))

list.append(6)  # Add a value at the end of the list (END)

list.sort()  #Sort the whole list (Ascending Order)

print(list)

list.sort(reverse = True)  #Sort the whole list (Descending Order)

#we can also write this for reversing
list.reverse()

list.insert(8 , 9 )    # add or insert a value to the list   ___.insert(idx , value )

list.remove(3)    #Remove the element (the value isn't idx , it's the element
list.pop(5)       #Remove the element using the IDX

print(list)


#Tuple :

tup = (2 , 4 , 6 , 8 , 10 , 12)        #This is Tuple   || And this is Immutable sequences of Value (We Cannot change their Value)
print(type(tup))


print((tup[0]))
print((tup[1]))
print((tup[2]))


#tup[0] = 5
#But this cannot be done


#The slicing of List is same as tuple

print(tup[0:3])


#TO find any value inside tuple we have to write like this
print(tup.index(4))         #We pass the value & the return value is the index


print(tup.count(6))   #We pass the value & get how many times the value is inside the TUPLE




#Practice :
#1. Enter the name of the three movie & store in a list

movie_list = []
X = input("Enter Your Fav movie name : ")
Y = input("Enter Your Fav movie name : ")
Z = input("Enter Your Fav movie name : ")
movie_list.append(X)
movie_list.append(Y)
movie_list.append(Z)

print(movie_list)


#2. Check if it is palindrome :
LL = [1 , 3 , 3 , 1]
LL_copy = LL.copy()
LL_copy.reverse()
if(LL == LL_copy):
    print("Palindrome")
else :
    print("Not Palindrome")


















