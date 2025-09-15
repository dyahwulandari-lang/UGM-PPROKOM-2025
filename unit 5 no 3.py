# Program menghitung Rata-Rata Nilai

# Minta pengguna memasukkan jumlah data nilai
Jumlah_nilai = int(input("Masukkan jumlah nilai yang ingin dihitung: "))

# Inisialisasi variabel untuk menyimpan total nilai
Total_nilai = 0

# Perulangan untuk menerima input nilai
for i in range(1, Jumlah_nilai + 1):
    nilai = float(input(f"Masukkan nilai ke-{i + 1}: "))
    Total_nilai += nilai

    # Hitung rata-rata
Rata_rata = Total_nilai / Jumlah_nilai

# Tampilkan hasil rata-rata
print(f"Rata-rata nilai dari {Jumlah_nilai} data adalah: {Rata_rata:.2f}")