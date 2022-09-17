"""
Setiap Hasil dari Operasi Komparasi adalah Boolean(True/False)

Operator Komparasi : > , < , >= , <= , == , != , is , is not

NOTE :
variabel yang ada nilainya, dia akan memakan memory dan disimpan dimemory, jadi kita bisa memanggil
berapapun variabel tersebut di codingan kita.
Sedangkan Literal adalah suatu nilai yg tidak ditampung oleh variabel, jadi langsung nilai aja, makannya disebut literal.
Literal tidak memakan memory karena dia literal, karena dia hidup dibaris code itu aja.
Contoh :
a = 4 // membuat variabel
hasil(a == 4) // 4 ini adalah literal dan dia tidak bisa dipanggil di baris code yg lain, karena si 4 ini tidak disimpan di variabel

INTINYA operator komparasi yg dapat bekerja pada syntax literal adalah > , < , >= , == , !=

Operator Komparasi is dan is not berguna untuk membandingkan memory/object
Contoh :
a = 4
b = 4
hasil(a is 4) // ini gk bisa, karena 4 itu literal
hasil(a is b) // ini bisa, karena a dan b adalah variabel yg ada nilainya dan identity nya disimpan di memory yg sama

"""

# Buat variabel a dan b yang menampung nilai 4 dan 2
a = 4
b = 2


# Lebih besar dari (>)
print('\n========= Lebih besar dari (>)')
hasil = a > 3 # Apakah a lebih besar dari 3?
print(a, '>', 3, '=', hasil) # Outpunya = 4 > 3 = True // karena 4 lebih besar dari 3

hasil = b > 3 # Apakah b lebih besar dari 3?
print(b, '>', 3, '=', hasil) # Outpunya = 2 > 3 = False // karena 2 lebih kecil dari 3

hasil = b > 2 # Apakah b lebih besar dari 2?
print(b, '>', 2, '=', hasil) # Outpunya = 2 > 2 = False // karena 2 tidak sama dengan dan harus lebih besar dari 2 kalau mau True


# Kurang dari (<) // Penjelasannya mirip sama yg diatas, jadi pahami aja dulu :)
print('\n========= Kurang dari (<)')
hasil = a < 3
print(a, '<', 3, '=', hasil)

hasil = b < 3
print(b, '<', 3, '=', hasil)

hasil = b < 2 # Coba ganti 2-nya menjadi 2.001, dan lihat hasilnya
print(b, '<', 2, '=', hasil) 


# Lebih besar dari sama dengan (>=)
print('\n========= Lebih besar dari sama dengan (>=)')
hasil = a >= 3
print(a, '>=', 3, '=', hasil)

hasil = b >= 3
print(b, '>=', 3, '=', hasil)

hasil = b >= 2
print(b, '>=', 2, '=', hasil) # Output = 2 >= 2 = True // karena 2 lebih dari sama dengan 2, maka hasilnya true


# Kurang dari sama dengan (<=)
print('\n========= Kurang dari sama dengan (<=)')
hasil = a <= 3
print(a, '<=', 3, '=', hasil)

hasil = b <= 3
print(b, '<=', 3, '=', hasil)

hasil = b <= 2
print(b, '<=', 2, '=', hasil) # Output = 2 <= 2 = True // karena 2 kurang dari sama dengan 2, maka hasilnya true


# Sama dengan (==) ini itu absolut, jadi apapun itu harus sama dengan komparasinya
print('\n========= Sama dengan (==)')
hasil = a == 3
print(a, '==', 3, '=', hasil)

hasil = b == 3
print(b, '==', 3, '=', hasil)

hasil = b == 2
print(b, '==', 2, '=', hasil) # Output = 2 == 2 = True // karena 2 sama dengan 2, maka hasilnya true

data_string = 'python'
hasil = data_string == 'python'
print(data_string, '==', 'python', '=', hasil) # Hasilnya = True, karena string 'python' sama dengan komparasinya yaitu string 'python'
# Ingat! ini harus benar benar sama, jadi kalau kita ganti value dari data_string nya menjadi 'Python', maka hasilnya akan false


# Tidak sama dengan (!=) // jadi ini kebalikan dari (==), kalau hasilnya True, maka jika menggunakan komparasi (!=) itu hasilnya false
print('\n========= Tidak sama dengan (!=)')
hasil = a != 3
print(a, '!=', 3, '=', hasil)

hasil = b != 3
print(b, '!=', 3, '=', hasil)

hasil = b != 2
print(b, '!=', 2, '=', hasil) # Output = 2 != 2 = False // karena 2 sama dengan 2, maka hasilnya false

data_string = 'Python'
hasil = data_string != 'python'
print(data_string, '!=', 'python', '=', hasil) # Hasilnya = True, karena string 'Python' tidak sama dengan komparasinya yaitu string 'python'


# is = sebagai komparasi object identity
print('\n========= Operator komparasi (is)')
x = 5 # ini adalah assignment membuat object
y = 6
print('nilai x = ',x,', idnya = ', hex(id(x)) ) # Outputnya = nilai x =  5 , idnya =  0x25bd05769b0 // idnya mungkin akan berbeda di kalian, tapi yg jelas 0x25bd05769b0 adalah idendity dari variabel x
print('nilai y = ',y,', idnya = ', hex(id(y)) ) # Outputnya = nilai y =  5 , idnya =  0x25bd05769b0
hasil = x is y
print('x is y =', hasil) # Output : x is y = true

"""
Jika variabel y diganti dengan angka 5 => hasil = x is 5
maka yg terjadi adalah si python akan mengeluarkan SyntaxWarning
Pesan Warningnya => SyntaxWarning: "is" with a literal. Did you mean "=="?
Jadi kalo 'is' mendingan jangan pake literal, karena nanti bakalan ada warning, pake aja == kalo mau pake literal

Untuk yg 'is not' itu sama aja dengan yang '!=', jadi dia kalau beda maka hasilnya True

"""





 