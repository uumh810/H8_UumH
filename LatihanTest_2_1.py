# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 15:32:33 2022

@author: 048115
"""
"""
nilai_akhir > 80 <100		#--> A
nilai_akhir > 70 <79		#--> B
nilai_akhir > 60 <69		#--> C
nilai_akhir > 50 <59		#--> D
nilai_akhir 0 < 49		#--> E

nilai_absen * 10%
nilai_tugas * 20%
nilai_uts * 30%
nilai_uas * 40%

nilai_total = akumulasi semua nilai
"""

nilai_akhir = int(input("masukan nilai kamu"))
nilai_absen = int(input("masukan absen kamu"))
nilai_uts = int(input("masukan nilai uts kamu"))
nilai_uas = int(input("masukan nilai uas kamu"))
total_nilai = (nilai_akhir*0.1) + (nilai_absen*0.2) + (nilai_uts*0.3) + (nilai_uas*0.4)
print("Hasil Nilai",total_nilai)

if total_nilai >80  <100:
    print("A")
elif total_nilai >70  <79:
    print("B")
elif total_nilai >60  <69:
    print("C")
elif total_nilai >50  <59:
    print("D") 
else:
    print("E")
