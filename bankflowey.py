'''
Desc: cost
author: vermilion10
date: november 2024
'''
biaya_awal = float(input('input biaya awal: '))
persen_bunga = float(input('input persen bunga: '))
total_biaya = biaya_awal + (biaya_awal * persen_bunga / 100)
print(f"{total_biaya:.2f}")
