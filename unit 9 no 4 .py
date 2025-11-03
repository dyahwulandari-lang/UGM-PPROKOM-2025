import numpy as np

nilai = [
[85, 80, 90],
[78, 82, 88],
[92, 90, 94],
[70, 68, 72],
[88, 85, 84],
[60, 75, 70],
[95, 92, 98],
[74, 70, 76],
[81, 85, 83],
[69, 72, 70],
[90, 88, 92],
[76, 80, 79],
[84, 86, 90],
[79, 82, 85],
[67, 70, 68],
[91, 94, 93],
[73, 78, 75],
[87, 84, 89],
[65, 68, 70],
[93, 90, 95],
[77, 80, 78],
[82, 84, 88],
[89, 85, 90],
[71, 74, 76]
]

# a. Tampilkan seluruh nilai menggunakan nested loop
for i, m in enumerate(nilai, start=1):
    tugas, uts, uas = m
    print(f"Mahasiswa ke-{i:02d} | Tugas: {tugas} | UTS: {uts} | UAS: {uas}")

# b. Menggunakan NumPy untuk menampilkan Rata-rata keseluruhan, Nilai tertinggi, Nilai terendah
arr = np.array(nilai)
print("Rata-rata keseluruhan:", np.mean(arr))
print("Nilai tertinggi:", np.max(arr))
print("Nilai terendah:", np.min(arr))