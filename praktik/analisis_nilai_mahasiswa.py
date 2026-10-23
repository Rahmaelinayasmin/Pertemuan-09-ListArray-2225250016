
# Praktik Pertemuan 09
# Analisis Nilai Mahasiswa Menggunakan List
# Tujuan: Mengolah data nilai dan menganalisis kelulusan mahasiswa.

# Fungsi untuk menghitung rata-rata
def rata_rata(data):
    if len(data) == 0:
        return 0

    return sum(data) / len(data)


# Fungsi untuk mengambil nilai yang memenuhi batas kelulusan
def nilai_lulus(data, batas=60):
    hasil = []

    for x in data:
        if x >= batas:
            hasil.append(x)

    return hasil


# Data nilai mahasiswa
nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]

# Mengolah data
banyak_data = len(nilai)
total = sum(nilai)
minimum = min(nilai) if banyak_data > 0 else 0
maksimum = max(nilai) if banyak_data > 0 else 0
rata = rata_rata(nilai)

# Menentukan kelulusan
batas_kelulusan = 60
lulus = nilai_lulus(nilai, batas_kelulusan)
jumlah_lulus = len(lulus)
jumlah_belum_lulus = banyak_data - jumlah_lulus

# Menampilkan hasil analisis
print("=" * 45)
print("       ANALISIS NILAI MAHASISWA")
print("=" * 45)

print(f"Daftar nilai       : {nilai}")
print(f"Banyak data        : {banyak_data}")
print(f"Total nilai        : {total}")
print(f"Rata-rata          : {rata:.2f}")
print(f"Nilai minimum      : {minimum}")
print(f"Nilai maksimum     : {maksimum}")
print(f"Batas kelulusan    : {batas_kelulusan}")
print(f"Daftar nilai lulus : {lulus}")
print(f"Jumlah lulus       : {jumlah_lulus}")
print(f"Belum lulus        : {jumlah_belum_lulus}")

print("=" * 45)
