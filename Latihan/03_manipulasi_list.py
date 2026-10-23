
# Latihan 3: Manipulasi List
# Tujuan: Mengubah, menambah, menyisipkan, dan menghapus elemen.

nilai = [75, 80, 65]

print("List awal:", nilai)

# Mengubah nilai pada indeks 1
nilai[1] = 82
print("Setelah mengubah elemen:", nilai)

# Menambahkan nilai pada akhir list
nilai.append(90)
print("Setelah append:", nilai)

# Menyisipkan nilai 70 pada indeks 1
nilai.insert(1, 70)
print("Setelah insert:", nilai)

# Menghapus elemen yang bernilai 65
nilai.remove(65)
print("Setelah remove:", nilai)
