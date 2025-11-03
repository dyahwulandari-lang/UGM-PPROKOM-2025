import numpy as np

A = np.array([[2, 4, 6],
              [1, 3, 5]])

B = np.array([[1, 1, 1],
              [2, 2, 2]])

# a. Penjumlahan dan pengurangan
tambah = A + B
kurang = A - B

print("Matriks A:\n", A)
print("\nMatriks B:\n", B)
print("\nHasil Penjumlahan (A + B):\n", tambah)
print("\nHasil Pengurangan (A - B):\n", kurang)


# b. Hitung perkalian matriks A x B^T
# Transpose dari matriks B
BT = B.T

# Perkalian A x B^T
hasil = np.dot(A, BT)

# Tampilkan hasil
print("\nTranspose B (B^T):\n", BT)
print("\nHasil Perkalian A x B^T:\n", hasil)