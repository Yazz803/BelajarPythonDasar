import time # menambahkan package/library
start_time = time.time()

print("Hello")
print("World")
print("Hello World")

print("test euy")
# ini adalah komen
a = 10 # ini adalah assignment (jadi disimpen dimemori variabelnya)
print(a) # menampilkan isi dari variabel a

"""
Ini disebutnya comment multiline
"""

for i in range(1, 3000):
    a = 10

print(time.time() - start_time, "detik")

# Code diatas akan dijalankan sesuai dari urutan code/baris nya
# contoh : 
# print(b) // "b" is not defined
# b = 2
# ini akan error, karena variabel b belum dibuat ketika memanggil print(b)

# Kita bisa mengcompile python ke yang namanya bytecode
# python -m py_compile Main.py // cara mengcompile nya // dijalankan di terminal
#  -m = tipe modenya
# py_compile = library python
# Main.py = nama file yg akan dicompile
# jika ada code yg diubah, maka kita harus re-compile, caranya sama kayak yg diatas

# Mengapa kita harus melakukan ini? dan apa bedanya?
# Yang dicompile akan lebih cepat daripada yang interpreted



