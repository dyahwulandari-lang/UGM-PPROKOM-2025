from array import array

# Bagian list
list_buah = ["Apel", "Mangga", "Jeruk"]
list_buah.append("Anggur")
list_buah.remove("Mangga")  # perbaikan dari pop("Mangga")
print("List Buah:", list_buah)

# Bagian array
arr_nilai = array('f', [85.5, 92.0, 78.5, 90.0])
arr_nilai.append(87.0)
nilai_pertama = arr_nilai[0]
print("Nilai pertama adalah:", nilai_pertama)
arr_nilai[2] = 20.0  # perbaikan dari "Delapan Puluh" jadi float
print("Array Nilai:", arr_nilai)