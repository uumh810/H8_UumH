# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 08:57:54 2022

@author: 048115
"""
# Function definition is here
def printinfo( name, nilai1,nilai2,nilai3,nilai4, nakhir):
   "This prints a passed info into this function"
   
   nakhir = (nilai1*0.1)+(nilai2*0.2)+(nilai3*0.3)+(nilai4*0.4)
   
   print("Name: ", name)
   print("nilai 1: ", nilai1)
   print("nilai 2: ", nilai2)
   print("nilai 3: ", nilai3)
   print("nilai 4: ", nilai4)
   print("nilai akhir: ", nakhir)

   return;

# Now you can call printinfo function
printinfo( name='a', nilai1=100, nilai2=80, nilai3=75, nilai4=88, nakhir=0)

