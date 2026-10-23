
# Latihan 5: Filter Kelulusan
# Tujuan: Menampilkan nilai yang memenuhi batas kelulusan 60.

nilai = [75, 55, 80, 60, 45, 90]
lulus = []

# Memeriksa setiap nilai
for x in nilai:
    if x >= 60:
        lulus.append(x)

print("Seluruh nilai:", nilai)
print("Nilai lulus:", lulus)
print(f"Jumlah mahasiswa lulus = {len(lulus)}")
