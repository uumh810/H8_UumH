# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def my_function(p, l):
    "Function untuk mengitung luas"
    print(p * l)

my_function(2,4)

def printme( str ):
   "This prints a passed string into this function"
   print(str)
   return;

printme("I'm first call to user defined function!")
printme("Again second call to the same function")

def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4]);
   print("Values inside the function: ", mylist)
   return

mylist = [10,20,30];
changeme( mylist );
print("Values outside the function: ", mylist)

def changeme( mylist ):
   "This changes a passed list into this function"
   mylist = [1,2,3,4]; # This would assig new reference in mylist
   print("Values inside the function: ", mylist)
   return

mylist = [10,20,30];
changeme( mylist );
print("Values outside the function: ", mylist)

def printme( str ):
   "This prints a passed string into this function"
   print(str)
   return;

printme(str = "Uum")

def printinfo( name, age ):
   "This prints a passed info into this function"
   print("Name: ", name)
   print("Age: ", age)
   return;

printinfo( age=4, name="a" )

def printinfo( name, age = 26 ):
   "This prints a passed info into this function"
   print("Name: ", name)
   print("Age: ", age)
   return;

printinfo( age=50, name="Nila" )
printinfo( name="Nila" )

# Function definition is here
def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print("Output is: ")
   print(arg1)
   for var in vartuple:
      print(var)
   return;

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50, "a" )

# Function definition is here
sum = lambda arg1, arg2: arg1 + arg2;

def sum(arg1, arg2):
    arg1 + arg2
    
# Now you can call sum as a function
print("Value of total : ", sum( 10, 20 ))
print("Value of total : ", sum( 20, 20 ))

# Function definition is here
def sum(arg1, arg2):
    # Add both the parameters and return them."
    total = arg1 + arg2
    total2 = total + arg1
    print("Inside the function : ", total)
    return total2

# Now you can call sum function
total = sum(10, 20)
print("Outside the function : ", total)

jumlahKucing = 20

def jumlahHewan():
    jumlahAnjing = 30
    return jumlahKucing + jumlahAnjing

def jumlahKelinci():
    return jumlahKucing + jumlahKucing

jumlahHewan()
jumlahKelinci()