stok_buku = {
    "Harry Potter": 10,
    "Laskar Pelangi": 15,
    "Bumi Manusia": 7,
    "Dilan 1990": 20
}

# 1) Tampilkan semua judul buku dan stoknya
print("Daftar Stok Buku:")
for Judul , stok in stok_buku.items():
    print(f"Buku: {Judul} - Stok: {stok}")

# 2) Minta input dari user untuk menambah buku baru
judul_baru = input("\nMasukkan judul buku baru: ")
stok_awal_baru = int(input("Masukkan jumlah stok awal: "))

stok_buku[judul_baru] = stok_awal_baru

print(f"Buku {judul_baru} berhasil ditambahkan dengan stok {stok_awal_baru}")
print("Dictionary stok buku terbaru:")
print(stok_buku)