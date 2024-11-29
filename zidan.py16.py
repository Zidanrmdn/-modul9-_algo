# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 10:20:39 2024

@author: sipalingpede
"""

def write(jadi):
    
    f = open("sipalingpede.txt", "w")
    
    f.write(jadi)
    
    f.close()
    
def read():
    
    f = open("sipalingpede.txt", "r")
    if f.mode == "r":
        contents = f.read()
    print (contents)
    
x = str(input("Masukkan Nama: "))
y = str(input("Masukkan Umur: "))
z = str(input("Masukkan Alamat: "))
q = str(input("Masukkan Email: "))
o = str(input("Masukkan Dosen Wali: "))
jadi = (f"Nama: {x}\n"f"Umur: {y}\n"f"Alamat: {y}\n"f"Email: {q}\n"f"Dosen Wali: {o}\n")
  
print("\n")
print("Berikut Ini Data Kamu")
write(jadi)
print("")
read()


