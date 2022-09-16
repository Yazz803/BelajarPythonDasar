"""
Casting adalah merubah dari satu tipe ke tipe lain.
tipe data = int, float, string, bool
Kita bisa menggunakan yang namanya operator casting.
Jadi misal angka 9 (int) bisa kita ubah ke tipe data (string)
"""


# merubah dari int ke float, string, dan bool
print("====INTEGER====")
data_int = 1
print("data = ", data_int, "- Bertipe = ", type(data_int))

data_float = float(data_int) # pake float() untuk merubah int ke float
data_str = str(data_int)
data_bool = bool(data_int)
print("data = ", data_float, "- Bertipe = ", type(data_float))
print("data = ", data_str, "- Bertipe = ", type(data_str))
print("data = ", data_bool, "- Bertipe = ", type(data_bool))
# jadi si boolean ini, ketika nilainya lebih dari atau kurang dari 0, maka nilainya True
# kalau sama dengan 0 maka hasilnya False


# merubah dari float ke int, string, dan bool
print("====FLOAT====")
data_float = 3.14
print("data = ", data_float, "- Bertipe = ", type(data_float))

data_int = int(data_float) # ini akan dibulatkan ke bawah
data_str = str(data_float)
data_bool = bool(data_float) # jika data_float = 0 maka akan False
print("data = ", data_int, "- Bertipe = ", type(data_int))
print("data = ", data_str, "- Bertipe = ", type(data_str))
print("data = ", data_bool, "- Bertipe = ", type(data_bool))


# merubah dari boolean ke int, string, dan string
print("====BOOLEAN====")
data_bool = False
print("data = ", data_bool, "- Bertipe = ", type(data_bool))

data_int = int(data_bool) 
data_str = str(data_bool)
data_float = float(data_bool) # jika data_bool = 0 maka akan False
print("data = ", data_int, "- Bertipe = ", type(data_int))
print("data = ", data_str, "- Bertipe = ", type(data_str))
print("data = ", data_float, "- Bertipe = ", type(data_float))


# merubah dari string ke int, string, dan bool
print("====STRING====")
data_string = "20" # jika stringnya kosong, maka boolean akan false
# data_string = "Yazz" # tidak bisa di casting ke int, karena ini adalah huruf
print("data = ", data_string, "- Bertipe = ", type(data_string))

data_int = int(data_string) # string harus angka
data_bool = bool(data_string) # string harus angka
data_float = float(data_string) # jika data_string = "" maka akan False
print("data = ", data_int, "- Bertipe = ", type(data_int))
print("data = ", data_bool, "- Bertipe = ", type(data_bool))
print("data = ", data_float, "- Bertipe = ", type(data_float))
