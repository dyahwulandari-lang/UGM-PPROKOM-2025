#Proses Penambahan
nilai = set({3,6,9,2,5,7})
nilai_baru = ({1,4,8,10})
nilai.update(nilai_baru)
print(nilai)

#Proses Penghapusan
nilai = set({3, 6, 9, 2, 5, 7})
nilai_baru = nilai.difference({3,5,7})
print(nilai_baru)
