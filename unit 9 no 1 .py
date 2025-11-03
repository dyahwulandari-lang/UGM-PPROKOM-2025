A = [
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
]

# a. Menampilkan lapisan pertama (indeks 0) menggunakan slicing
print(A[0][:])

# b. Menampilkan semua elemen kolom terakhir dari setiap baris dan lapisan
print("Elemen kolom terakhir dari setiap baris dan lapisan:")
for i, lapisan in enumerate(A):         # i = indeks lapisan
    for j, baris in enumerate(lapisan): # j = indeks baris di dalam lapisan
        nilai = baris[-1]               # elemen terakhir pada baris
        print(f"Lapisan {i}, Baris {j} -> {nilai}")