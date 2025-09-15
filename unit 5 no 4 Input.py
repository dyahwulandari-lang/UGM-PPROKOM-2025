# Cetak pola 1..5 bintang (bintang dipisah spasi)
n = 5 
for i in range(1, n + 1):
    for j in range(i):
        print('*', end=' ')
    print()