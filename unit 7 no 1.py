harga_buah = {
    "Apel": 15000,
    "Jeruk": 10000,
    "Anggur": 25000
}

print(f"Harga Jeruk: Rp{harga_buah['Jeruk']}")

harga_buah["Mangga"] = 12000
print("Dictionary buah-buahan terbaru setelah menambah Mangga:", harga_buah)

harga_buah["Anggur"] = 20000
print("Dictionary buah-buahan terbaru setelah memperbarui harga Anggur:", harga_buah)

harga_buah.pop("Jeruk")
print("Dictionary buah-buahan terbaru setelah menghapus Jeruk:", harga_buah)