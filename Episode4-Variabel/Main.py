# Variabel adalah tempat menyimpan data

# Penamaan Variabel
# nilai y = 5 // ini gk bisa, karena gk boleh ada spasinya ,jadi harus pake "_"
# nilai_y = 5 // ini bisa/boleh, tanda "-" ini juga gk boleh, yaa coba2 aja coy
# 10juta = 100000 // ini gk boleh, karena kita tidak bisa menaruh angka didepan variabelnya
# juta10 = 100000 // kalo ini boleh
# nilaiZ = 10 // ini boleh

a = 10 # jadi si a ini menyimpan nilai 10 (integer)
# jadi si a ini adalah variabel, dan 10 adalah valuenya
# tanda "=" adalah asignment

# menaruh/assignment nilai
x = 10
y = 5
panjang = 1000

# kita bisa memanggil variabel sebanyak apapun
# ini adalah pemanggilan pertama
print("Nilai a = ", a)
print("Nilai x = ", x)
print("Nilai panjang = ", panjang)


# ini adalah pemanggilan kedua
print("Nilai a = ", a)
# jika ada nama variabel yg sama, maka valuenya akan ditimpa
a = 7
print("Nilai a = ", a)

# assignment indirect // jadi dia tidak langsung ke dalam sebuah angka, tapi langsung ke variabel sebelumnya
b = a
print("Nilai b = ", b)
