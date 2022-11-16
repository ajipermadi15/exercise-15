"""
Bersihkan kode ini!

Dengan materi clean code yang sudah dipelajari, aturlah sedemikian rupa sehingga kode di bawah bisa menjadi lebih readable.
"""
import numpy as np

def intro():
    print('-'*60)
    print('LUAS dan Keliling BANGUN DATAR')
    print('-'*60)
    print('1. Segitiga Siku-siku')
    print('2. Persegi')
    print('3. Persegi Panjang')
    print('4. Lingkaran')
    print('-'*60)


def segitiga(alas, tinggi):
    sisi_miring = np.sqrt(alas**2 + tinggi**2)
    keliling = alas + tinggi + sisi_miring
    luas = 0.5 * alas * tinggi

    return keliling, luas


def persegi(sisi):
    keliling = 4 * sisi
    luas = sisi ** 2

    return keliling, luas


def persegi_panjang(panjang, lebar):
    keliling = 2 * (panjang + lebar)
    luas = panjang * lebar

    return keliling, luas


def lingkaran(radius):
    keliling = 2 * np.pi * radius
    luas = np.pi * (radius ** 2)

    return keliling, luas


while True:
    intro()

    tipe = int(input('Masukkan bangun datar yang diinginkan (1-4): '))

    if tipe == 1:
        alas = float(input('Masukkan nilai alas: '))
        tinggi = float(input('Masukkan nilai tinggi: '))
        keliling, luas = segitiga(alas, tinggi)
        print(f'Keliling segitiga siku-siku dengan alas {alas} satuan dan tinggi {tinggi} satuan adalah {keliling} satuan.')
        print(f'Luas segitiga siku-siku dengan alas {alas} satuan dan tinggi {tinggi} satuan adalah {luas} satuan.')
    elif tipe == 2:
        sisi = float(input('Masukkan nilai sisi: '))
        keliling, luas = persegi(sisi)
        print(f'Keliling persegi dengan sisi {sisi} satuan adalah {keliling} satuan.')
        print(f'Luas persegi dengan sisi {luas} satuan adalah {luas} satuan.')
    elif tipe == 3:
        panjang = float(input('Masukkan nilai panjang: '))
        lebar = float(input('Masukkan nilai lebar: '))
        keliling, luas = persegi_panjang(panjang, lebar)
        print(f'Keliling persegi panjang dengan panjang {panjang} satuan dan lebar {lebar} satuan adalah {keliling} satuan.')
        print(f'Luas persegi panjang dengan panjang {panjang} satuan dan lebar {lebar} satuan adalah {luas} satuan.')
    elif tipe == 4:
        radius = float(input('Masukkan nilai radius: '))
        keliling, luas = lingkaran(radius)
        print(f'Keliling lingkaran dengan radius {radius} satuan adalah {keliling} satuan.')
        print(f'Luas lingkaran dengan radius {radius} satuan adalah {luas} satuan.')
    else:
        print('Pastikan masukkan pilihan yang benar (1-4)!')

    repeat = input('Apakah ingin menghitung ulang? (Y/N): ')

    if repeat.lower() == 'n':
        break
