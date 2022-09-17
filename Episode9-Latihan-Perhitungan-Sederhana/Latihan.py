"""
Tugasnya adalah mencari rumus untuk mengkonversi dari fahrenheit
ke kelvin dan kelvin ke fahrenheit

Hint : ubah dulu fahrenheit/kelvin ke celcius, nah nanti di celcius itu kita bisa ubah ke fahrenheit dan kelvin
Rumus Fahrenheit->Celcius = (5/9)*(F-32)
Rumus Kelvin->Celcius = K-273
"""

# Fahrenheit -> Kelvin
print("\n PROGRAM KONVERSI FAHRENHEIT KE KELVIN \n")
fahrenheit = float(input('Masukan suhu (Fahrenheit): '))
print('Suhu fahrenheit adalah : ', fahrenheit, 'F')
F_ke_C = (5/9)*(fahrenheit-32) # ubah fahrenheit ke celcius
C_ke_K = F_ke_C+273 # ubah celcius ke kelvin
print('Jika di konversi ke Kelvin, maka hasilnya : ', C_ke_K, 'K')

print("===========================================")

print("\n PROGRAM KONVERSI FAHRENHEIT KE KELVIN \n")
kelvin = float(input('Masukan suhu (Kelvin) : '))
print('Suhu Kelvin adalah : ', kelvin, 'K')
K_ke_C = kelvin-273 # ubah kelvin ke celcius
C_ke_F = (9/5)*K_ke_C+32
print('Jika di konversi ke Fahrenheit, maka hasilnya : ', C_ke_F, 'F')



print('\n')