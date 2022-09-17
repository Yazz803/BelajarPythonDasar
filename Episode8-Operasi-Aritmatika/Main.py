"""
Operasi Aritmaika :
1. tambah (+)
2. kurang (-)
3. kali (*)
4. bagi (/)
5. Eksponen/pangkat (**)
6. sisa bagi/modulus (%)
7. floor division (//) -> pembulatan dari pembagian, misal 10 / 3 = 3.33...
   Kalau kita pake floor division itu kita bisa membulatkan angkanya jadi 3

Prioritas operasi / operational precedence :
Contoh = 3 ** 2 * 4 + 3 / 2 - 2 % 4 // 3
Urutannya yg akan dikerjakan dulu adalah = 
- ()
- eksponen
- perkalian/pembagian/modulus/floordivision
- pertambahan
- pengurangan

Untuk lebih jelasnya lihat aja di gambar

"""


a = 10
b = 3

# Operasi tambah
hasil = a + b
print("Pertambahan dari ", a ," + ", b , "= ",hasil)
# Output = Pertambahan dari  10  +  3 =  13

# Operasi kurang
hasil = a - b
print("Pengurangan dari ", a ," - ", b , "= ",hasil)
# Output = Pengurangan dari  10  -  3 =  7

# Operasi kali
hasil = a * b
print("Perkalian dari ", a ," * ", b , "= ",hasil)
# Output = Perkalian dari  10  *  3 =  30

# Operasi pembagian
hasil = a / b
print("Pembagian dari ", a ," / ", b , "= ",hasil)
# Output = Pembagian dari  10  /  3 =  3.3333333333333335 -> jadi float

# Operasi eksponen
hasil = a ** b
print("Pangkat dari ", a ," ** ", b , "= ",hasil)
# Output = Pangkat dari  10  **  3 =  1000
# Jadi ini dibacanya 10 pangkat -3 hasilnya 0.001
# Jika -3 diganti jadi 3, maka hasilnya 1000 karena 10 pangkat 3 (10x10x10) adalah 1000

# Operasi modulus
hasil = a % b
print("Sisa bagi dari ", a ," % ", b , "= ",hasil)
# Output = Sisa bagi dari  10  %  3 =  1
# Output = Sisa bagi dari  10  %  -3 =  -2 // ini saya juga kurang ngerti kenapa hasilnya -2, coba deh kalian ulik sendiri
# Output = Sisa bagi dari  10  %  2 =  0 // karena tidak ada sisa dari pembagian
# Jadi misal 11 % 3 itu hasilnya 2, karena 3 * 3 = 9, berarti 11 - 9 = 2 (ini sisa baginya)

# Operasi floor division / dibulatkan ke bawah
hasil = a // b
print("Pembulatan kebawah dari ", a ," // ", b , "= ",hasil)
# Output = Pembulatan kebawah dari  10  //  3 =  3
# Biasanya kan kalo 10 / 3 itu hasilnya 3.333335, itu bisa kita bulatkan
# dengan menggunakan floor division, jadi hasilnya nanti 3

# Prioritas Operasi
x = 3
y = 2
z = 4
hasil = x ** y * z + x / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=', hasil) 
# Output = 3 ** 2 * 4 + 3 / 2 - 2 % 4 // 3 = 37.5

o = 3
i = 5
print(o % i)
# Kalau angka pertama itu lebih besar dari angka kedua, jika dimodulus, yg tampil adalah angka pertama

# Tanda kurung akan mengambil langkah paling pertama
hasil = ( x + y ) * z
print('(',x,'+',y,')','*',z,'=',hasil)