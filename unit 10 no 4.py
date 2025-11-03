# Nama : Dyah Wulandari
# NIM  : 25/567655/SV/27221

import math

# Fungsi-fungsi menggunakan lambda
tambah = lambda a, b: a + b
kurang = lambda a, b: a - b
kali = lambda a, b: a * b
bagi = lambda a, b: a / b if b != 0 else "Tidak bisa dibagi dengan nol!"
pangkat = lambda a, b: a ** b
akar = lambda a: math.sqrt(a) if a >= 0 else "Tidak bisa akar bilangan negatif!"

# Program utama
while True:
    print("\n=== KALKULATOR MATEMATIKA SEDERHANA ===")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Perpangkatan")
    print("6. Akar Kuadrat")
    print("7. Keluar")

    pilihan = input("Pilih menu (1-7): ")

    if pilihan == '1':
        a = float(input("Masukkan bilangan pertama: "))
        b = float(input("Masukkan bilangan kedua: "))
        print("Hasil:", tambah(a, b))

    elif pilihan == '2':
        a = float(input("Masukkan bilangan pertama: "))
        b = float(input("Masukkan bilangan kedua: "))
        print("Hasil:", kurang(a, b))

    elif pilihan == '3':
        a = float(input("Masukkan bilangan pertama: "))
        b = float(input("Masukkan bilangan kedua: "))
        print("Hasil:", kali(a, b))

    elif pilihan == '4':
        a = float(input("Masukkan bilangan pertama: "))
        b = float(input("Masukkan bilangan kedua: "))
        print("Hasil:", bagi(a, b))

    elif pilihan == '5':
        a = float(input("Masukkan bilangan: "))
        b = float(input("Masukkan pangkat: "))
        print("Hasil:", pangkat(a, b))

    elif pilihan == '6':
        a = float(input("Masukkan bilangan: "))
        print("Hasil:", akar(a))

    elif pilihan == '7':
        print("Program selesai. Terima kasih!")
        break

    else:
        print("Pilihan tidak valid, silakan coba lagi.")