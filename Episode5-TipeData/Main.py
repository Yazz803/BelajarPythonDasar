# Tipe data apa aja yang ada di Python
"""
1. Angka satuan (integer) -> 1,2,9,11,2022 // pokoknya yg gk ada komanya
2. Angka dengan koma (Float) -> 3.14 , 90.11 , 2.002 // tipe double itu gk ada di py, adanya float ajah
3. Kumpulan karakter (String) -> "Hello" , "Hello World" , "Angka 20" // jadi karakter apa aja yg ada di keyboard bakalan di tampilin, kecuali "\" ya setau saya itu
4. Tipe data Biner (Boolean) -> True/False // biasanya ini digunakan di dalam pengondisian/percabangan
"""
# Tipe data khusus
"""
1. Bilangan kompleks/data kompleks
"""

# Tipe data dari bahasa C
"""
di Python gk ada char, long, double. Terus gmn caranya supaya kita bisa
pakai bahasa C? karena si python ini dibuatnya pake bahasa C, kita bisa
pakai bahasa C disini tipe datanya. Tapi sebelum itu kita harus import dulu
si package-nya atau library-nya
"""

# Integer
data_integer = 911
print("data : ",data_integer)
print("- bertipe : ", type(data_integer))
print("\n") # untuk menambah baris baru/ New Line
# Output = data :  911 , bertipe :  <class 'int'>
# jadi ini tu maksudnya tipe data dari variabel data_integer adalah int

# Float
data_float = 3.14
print("data : ",data_float)
print("- bertipe : ", type(data_float))
print("\n") # untuk menambah baris baru/ New Line

# String
data_string = "Saya Yazid dan umur saya 17 tahun, *&$*#01239 0.9"
print("data : ",data_string)
print("- bertipe : ", type(data_string))
print("\n") # untuk menambah baris baru/ New Line

# Boolean
data_bool = True
print("data : ",data_bool)
print("- bertipe : ", type(data_bool))
print("\n") # untuk menambah baris baru/ New Line

# Data Kompleks
data_complex = complex(5,6)
print("data : ",data_complex)
print("- bertipe : ", type(data_complex))
# output : data : (5+6j) "j" nya itu imaginare
print("\n") # untuk menambah baris baru/ New Line

# Tipe data C
from ctypes import c_double, c_char, c_long # jadi kita bisa menggunakan tipe data yg ada di bahasa C dengan memanggil package ini
    
data_c_double = c_double(10.5)
print("data : ",data_c_double)
print("- bertipe : ", type(data_c_double))
