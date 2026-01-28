# Lecture 4
# Dictionary & Set in Python

# Dictionary in Python: it stores Key & Value in pairs
# it is unorder , mutable(changeable) , don't allow duplicate keys
user = {
    # "key" : "value" ,
    "name": "Anik",
    "age": 35,
    "cgpa": 3.80,
    "learning": "Python",
    "male": True
}
print(user)

print("\n")
# We can also put list & tuples in the Dictionary
anik = {
    "list_of_movies": ["bh6", "Titanic"],
    "tup_of_games": (12, 13),
}
print(anik)
print(type(anik))

print("\n")
# We can make our key into float & int value :
ctg = {
    12: 15.99,
    12.34: 11,
    True: "male",
    "name": "anik"
}
print(ctg)

# How to access value of a dictionary : By using the key
print(ctg[12])
print(ctg[12.34])
print(ctg["name"])

# we can also assign new names like
ctg["name"] = "Zafrox"  # We are overwriting here

# we can also make new items
ctg["surname"] = "Kazi"  # We have added it
print(ctg)

# Nested Dictionaries : a dictionary under another one
mother_variable = {
    "name": "X",
    "age": 40,
    "gender_female": True,

    "son": {
        "name": "Y",
        "age": 23,
        "gender_female": False
    }
}
print(mother_variable["son"]["age"])

# Imp functions of Dictionaries :
# 1. to print all the keys :
print(mother_variable.keys())

# 2. to print the size / length :
print(len(mother_variable))  # total number of keys (doesn't count the nested keys only the main nested one )

# 3. to print all the values :
print(mother_variable.values())

# 4. to print all the keys & values as pairs :
print(mother_variable.items())
pairs = list(mother_variable.items())  # we made the dictionary into pairs
print(pairs[0])  # to access the first value of the pair

# to get the value using the keys :
print(mother_variable.get("name"))  # we send key & got the value

# to add new items to the existing dictionary :
new_dict = {"city": "Dhaka"}
mother_variable.update(new_dict)
print(mother_variable)

# ITEMS in python :
# to store unique values in python & the number must be mutable (we can also put strings here)
# we can't store list & dictionary in set
setf = {1, 2, 2, 3, 4}
print(setf)
print(type(setf))

setg = {"anik", "anik", "hello world", 1, 1, 2, 2, 4, 5}
print(setg)  # set doesn't follow any order like it doesn't follow any order when print

# Empty set
set1 = {}  # this is not an empty set it's an empty dictionary
print(type(set1))

set2 = set()  # this is an empty set
print(type(set2))

# Mathod or functions of sets :
sett = {1, 2, 3, 4, 5, 5, 6, 6}
print(sett)

sett.add(9)  # to add values in set
print(sett)

sett.remove(6)  # to remove value in set
print(sett)

sett.pop()  # to remove random value of a set
print(sett)

sett.clear()  # to clear the whole set
print(sett)

# Set methods

# 1. Union of a set = combine both sets & return a new set
# 2. Intersection of a set = combine common of the set & return a new set


setx = {1, 2, 3}
sety = {3, 4, 5}


# to use union we write
print(setx.union(sety))      # return all the elements


# to use intersection we write
print(setx.intersection(sety))  # return only the common elements

# Practice a problem :

# make a set for 9 & 9.0  both have to be in separate set [as set treats 9 & 9.0 as 9]

seta = {9 , 9.0}
print(seta)   #as set treats them as 9 so we have to think differently


seta = {9 , "9.0"}
print(seta)




















