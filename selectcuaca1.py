# -*- coding: utf-8 -*-
"""
Created on Mon May 15 10:05:31 2023

@author: ASUS
"""

import mysql.connector as sql
import dbpustaka as ptk

#1 buat koneksi
koneksi = sql.connect(
    host = "localhost",
    user = "root",
    passwd= "123",
    database = "kluxx")
#2 buat cursor
kursor = koneksi.cursor()
#3 buat query
perintah = "select tanggal, tmpmin, tmpmax, tmpavg, rainfall\ from cuaca\ where tanggal < '2021-03-15'\
    order by humidity"
#4 jalan query
kursor.execute(perintah)
#5 pindahkan isi kursor ke dalam list
datalist = [["stament", "tanggal", "tmpmin", "tmpmax", "tmpavg", \
             "tmpavg", "kelembaban", "curah hujan", \
             "cloud", "windmax", "winddir", "winavg", \
             "arah angin"   ]]
for data in kursor:
    #masukkan data ke dalam list 
    datalist.append(data)
    
    print (data)

#6 simpan isi list
ptk.saveCSV("query1.CSV", datalist)

#7 tutup cursor dan koneksi
kursor.close()
koneksi.close()