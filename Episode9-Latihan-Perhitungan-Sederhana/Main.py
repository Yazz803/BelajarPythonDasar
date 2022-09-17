# Program konversi celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input('Masukan suhu dalam Celcius : '))
print('Suhu adalah ', celcius, 'C')

# Reamur -> rumus -> (4/5)*C
reamur = (4/5)*celcius
print('Reamurnya adalah : ', reamur, 'R')

# Fahrenheit -> rumus -> (9/5)*C+32
fahrenheit = (9/5)*celcius+32
print('Fahrenheitnya adalah : ', fahrenheit, 'F')

# Kelvin -> rumus -> C+273
kelvin = celcius+273
print('Kelvinnya adalah : ', kelvin, 'K')

print('\n') # New line supaya rapi di terminalnya