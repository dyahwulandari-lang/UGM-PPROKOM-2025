[
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
] 

# a. Membuat matriks identitas berukuran 4x4 dengan nested list comprehension
identitas = [[1 if i == j else 0 for j in range(4)] for i in range(4)]

# Menampilkan hasil
print("Matriks identitas 4x4:")
for baris in identitas:
    print(baris)


# b. Matriks identitas dengan menambahkan variabel input n

# Meminta input dari pengguna
n = int(input("Masukkan ukuran matriks identitas (n): "))

# Membuat matriks identitas sesuai ukuran n
identitas = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

# Menampilkan hasil
print(f"\nMatriks identitas {n}x{n}:")
for baris in identitas:
    print(baris)