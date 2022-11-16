"""
Perbaiki kode ini!

Diberikan list data yang berisi tuple informasi mahasiswa, (nama, nim, nilai akhir). 
Dari data tersebut, akan ditentukan indeks yang diperoleh berdasarkan nilai akhir dari setiap mahasiswa.
Indeks yang diperoleh memenuhi aturan berikut:

A : 90 <= x <= 100
B : 80 <= x < 90
C : 70 <= x < 80
D : 60 <= x < 70
E : x < 60

Setiap mahasiswa dikatakan `Lulus` jika memperoleh indeks A, B, atau C, dan dikatakan mengulang jika memperoleh indeks D dan E.
"""

data_mahasiswa = [('Aurel', 101, 80), ('Bon', 102, 79), ('Cici', 103, 92), ('Domixus', 104, 65), ('Enggar', 105, 55)]

for nama, nim, na in data_mahasiswa:
    if na > 90:
        grade = 'A'
    elif na < 90:
        grade = 'B'
    elif na < 80:
        grade = 'C'
    elif na < 70:
        grade = 'D'
    elif na < 60:
        grade = 'E'

    if grade == 'A' or 'B' or 'C':
        status = 'Lulus'
    else:
        status = 'Mengulang'

    print(f'Mahasiswa bernama {nama} dengan NIM {nim} dinyatakan {status} pada mata kuliah ini dengan perolehan indeks {grade}.')