"""
Perbaiki kode ini!

Definisi: Bilangan prima merupakan bilangan bulat positif yang HANYA habis dibagi oleh 1 dan bilangan itu sendiri.
Perbaiki kode di bawah sehingga dapat berjalan sebagaimana mestinya.
"""

def prime_number(number):
    result = 'Bilangan prima'
    for num in range(2, int(number/2) + 1):
        if number % 2 == 0:
            result = 'Bukan bilangan prima'
            #break

    return result

number = int(input('Masukkan angka: '))
if number > 0:
    result = prime_number(number)
    print(f'Angka {number} adalah {result}')
else:
    print('Silahkan masukkan angka yang valid! (bilangan bulat positif)')