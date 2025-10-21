# 1. Mengimpor modul array
from array import array

# 2. Membuat sebuah array integer dengan 5 nilai angka bebas
data = array('i', [10, 20, 30, 40, 50])

# 3. Menampilkan array beserta panjangnya
print("Isi array:", data)
print("Jumlah elemen dalam array:", len(data))

# 4. Menghitung jumlah total elemen
total = sum(data)
print("Jumlah total elemen:", total)

# 5. Menghitung rata-rata elemen array
rata_rata = total / len(data)
print("Nilai rata-rata elemen:", rata_rata)