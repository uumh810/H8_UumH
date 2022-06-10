# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 14:54:20 2022

@author: 048115
"""

hargaBuku = int(input("masukan harga buku"))
jumlah = int(input("masukan jumlah yang dibeli"))
uang = int(input("masukan jumlah uang"))
total = hargaBuku + jumlah - uang
print ("total belanja",total)

if uang > hargaBuku:
    print("beli buku")
elif uang == hargaBuku:
    print("maaf hanya bisa beli secukupnya")
else:
    print("maaf anda kurang beruntung")
    
