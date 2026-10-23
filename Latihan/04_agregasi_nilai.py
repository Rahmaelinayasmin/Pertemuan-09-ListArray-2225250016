
# Latihan 4: Agregasi Nilai
# Tujuan: Menghitung total, rata-rata, minimum, dan maksimum.

nilai = [75, 80, 65, 90, 88]

total = sum(nilai)
banyak_data = len(nilai)
rata_rata = total / banyak_data
minimum = min(nilai)
maksimum = max(nilai)

print("Daftar nilai:", nilai)
print(f"Total nilai = {total}")
print(f"Rata-rata = {rata_rata:.2f}")
print(f"Nilai minimum = {minimum}")
print(f"Nilai maksimum = {maksimum}")
