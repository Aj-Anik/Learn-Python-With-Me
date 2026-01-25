#Lecture 2
# Strings & Conditional Statements


a = "Aj"
b = "Anik"
print(a+b) #String Concatenation

print(len(b)) #Length of String

#how to use next line in Python

str1 = "Hello I am Anik .\nI love my country"  #By using \n
print(str1)

#If we want tab space we use \t
str2 = "International Islamic University \tChittagong"
print(str2)

str3 = "World Wide Web"
print(str3[3])


#Slicing Of String
str3 = "World Wide Web"
print(str3[0:3]) #to access the 0th to 3rd index
print(str3[ :5]) #Empty in starting means from 0th (ending idx is excluded)
print(str3[4: ]) #Empty in the end means from x index to len(str3)


#Python has negative Idx
# A   p   p   l   e
#-5  -4  -3  -2  -1

#Some String Functions (Important)

#  1.
str4 = "I love Bangladesh"
print(str4.endswith("desh"))   # this checks if the string has any substr of B & always returns Boolean

str4.capitalize()  # make the first char Capital || And it works only when we call the function once , but won't change in the main string

print(str4.replace("Bangladesh" , "USA"))   #To replace the string

print(str4.find("love") )    # To find any substr  && Return the first idx of the searching substr and if we don't find it we will get -1

print(str4.count("l")) #To count the substr





# !!!!!!!!! Conditions

"""
if(condition) :
    statement 1
elif(condition) :
    statement 2
else : 
    statement (N times)
"""

x = int(input("Enter Your Age : "))
if x >= 18:
    var = {
        print("You are eligible for Vote\n")
    }
elif x < 18:
    var = {
        print("You Aren't eligible for vote\n")
    }


#Using Nested Loops || Multiple if conditions





