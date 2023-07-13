print("Pilih operasi:")
print("1. Tambah (+)")
print("2. Kurang (-)")
print("3. Kali (x)")
print("4. Bagi (/)")
print('\n')
pilihan = input("Masukkan Pilihan : ")

angka1 = float(input("Masukkan Angka Pertama : "))
angka2 = float(input("Masukkan Angka Kedua : "))

def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    return a / b

if pilihan == '1':
    print(angka1, "+", angka2, "=", tambah(angka1, angka2))
elif pilihan == '2':
    print(angka1, "-", angka2, "=", kurang(angka1, angka2))
elif pilihan == '3':
    print(angka1, "*", angka2, "=", kali(angka1, angka2))
elif pilihan == '4':
    print(angka1, "/", angka2, "=", bagi(angka1, angka2))
else:
    print("Pilihan tidak valid")
    
