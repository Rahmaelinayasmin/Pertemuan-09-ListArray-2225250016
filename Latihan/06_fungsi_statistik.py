
# Latihan 6: Fungsi Statistik
# Tujuan: Membuat fungsi untuk menghitung rata-rata list.

def rata_rata(data):
    # Menangani list kosong agar tidak terjadi pembagian nol
    if len(data) == 0:
        return 0

    return sum(data) / len(data)


nilai = [75, 80, 65, 90, 88]

hasil = rata_rata(nilai)

print("Daftar nilai:", nilai)
print(f"Rata-rata = {hasil:.2f}")
