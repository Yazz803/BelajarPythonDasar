# Kita bisa menginputkan dan menampilkan data dari hasil inputan user
# Defaultnya ketika user input data dan ditampilkan, itu tipe datanya string
# Jika ingin diubah ke int, float, atau boolean, itu bisa kita gunakan casting
# Jadi Kita bisa pakai operator casting untuk mengubah tipe data dari input

# Data yang dimasukan pasti string
data = input("Masukan data : ")
print("Data = ", data, " - Bertipe = ", type(data))


# Jika kita ingin mengambil innteger
angka = float(input("Masukan angka : ")) # di casting/diubah
# angka = int(input("Masukan angka : ")) # di casting/diubah
print("Angka = ", angka, " - Bertipe = ", type(angka))


# lalu bagaimana dengan boolean?
# Ini harus kita casting dulu ke integer
biner = bool(int(input("masukan nilai boolean : "))) # jadi ini kita casting dulu ke boolean, lalu ke integer
print("Boolean = ", biner, " - Bertipe = ", type(biner))

