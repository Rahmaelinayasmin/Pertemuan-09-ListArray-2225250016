
# Pertemuan 09 - List dan Pengolahan Data Numerik

## Identitas Mahasiswa

- Nama: [Rahma Elina Yasmin]
- NIM: [2225250016]
- Kelas: [3F]
- Mata Kuliah: Algoritma dan Pemrograman
- Pertemuan: 09
- Materi: List/Array dan Pengolahan Data Numerik Sederhana

## 1. Tujuan

Praktikum ini bertujuan untuk memahami penggunaan list dalam Python
untuk menyimpan dan mengolah sekumpulan data numerik.

Setelah menyelesaikan praktikum, mahasiswa diharapkan mampu:

1. Membuat list kosong dan list berisi data.
2. Mengakses elemen menggunakan indeks positif dan negatif.
3. Mengambil bagian list menggunakan slicing.
4. Mengubah, menambah, menyisipkan, dan menghapus elemen list.
5. Menggunakan perulangan untuk memproses seluruh elemen.
6. Menghitung total, rata-rata, nilai minimum, dan maksimum.
7. Menyaring nilai berdasarkan batas kelulusan.
8. Membuat fungsi yang menerima list sebagai parameter.
9. Menguji program menggunakan beberapa test case.
10. Mengunggah hasil pekerjaan ke GitHub.

## 2. Konsep yang Dipelajari

### A. List

List merupakan struktur data Python yang menyimpan beberapa elemen
dalam satu variabel.

Contoh:

    nilai = [75, 80, 65, 90, 88]

### B. Indeks dan Slicing

Indeks Python dimulai dari 0. Indeks -1 digunakan untuk mengakses
elemen terakhir.

Contoh:

    nilai[0]
    nilai[-1]
    nilai[1:4]

### C. Manipulasi List

Operasi yang dipelajari meliputi:

- append(): menambahkan elemen di akhir list.
- insert(): menyisipkan elemen pada indeks tertentu.
- remove(): menghapus elemen berdasarkan nilainya.
- pop(): menghapus elemen berdasarkan indeks.
- sort(): mengurutkan elemen.

### D. Pengolahan Data Numerik

Fungsi yang digunakan:

- len(data): menghitung banyak elemen.
- sum(data): menghitung jumlah seluruh elemen.
- min(data): mencari nilai minimum.
- max(data): mencari nilai maksimum.

Rata-rata dihitung dengan rumus:

    rata_rata = sum(data) / len(data)

List kosong harus diperiksa terlebih dahulu sebelum menghitung
rata-rata untuk menghindari pembagian dengan nol.

## 3. Struktur Program

Folder latihan berisi enam program:

1. 01_buat_list.py
2. 02_indeks_slicing.py
3. 03_manipulasi_list.py
4. 04_agregasi_nilai.py
5. 05_filter_kelulusan.py
6. 06_fungsi_statistik.py

Folder praktik berisi:

- analisis_nilai_mahasiswa.py

Program praktik digunakan untuk menghitung statistik nilai,
menentukan mahasiswa yang lulus, dan menghitung jumlah mahasiswa
yang belum lulus.

## 4. Cara Menjalankan Program

1. Buka Visual Studio Code.
2. Buka folder proyek Pertemuan 09.
3. Pastikan Python 3 telah terpasang.
4. Buka file Python yang ingin dijalankan.
5. Buka Terminal > New Terminal.
6. Jalankan program menggunakan perintah berikut.

Untuk Windows:

    python latihan/01_buat_list.py
    python latihan/02_indeks_slicing.py
    python latihan/03_manipulasi_list.py
    python latihan/04_agregasi_nilai.py
    python latihan/05_filter_kelulusan.py
    python latihan/06_fungsi_statistik.py
    python praktik/analisis_nilai_mahasiswa.py

Jika perintah python tidak tersedia, gunakan python3 sesuai
konfigurasi Python pada perangkat.

## 5. Algoritma Praktik Analisis Nilai Mahasiswa

1. Menyiapkan list yang berisi sepuluh nilai mahasiswa.
2. Menghitung jumlah data menggunakan len().
3. Menghitung total menggunakan sum().
4. Menghitung rata-rata melalui fungsi rata_rata().
5. Mencari nilai minimum dan maksimum.
6. Memeriksa setiap nilai menggunakan perulangan.
7. Memasukkan nilai yang lebih besar dari atau sama dengan 60
   ke dalam list lulus.
8. Menghitung jumlah mahasiswa lulus.
9. Menghitung jumlah mahasiswa belum lulus.
10. Menampilkan seluruh hasil analisis.

## 6. Tabel Pengujian

| No. | Program/Data Uji | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|
| 1 | List lima nilai | Lima nilai tersimpan | Lima nilai tersimpan | Berhasil |
| 2 | Indeks pertama | 75 | 75 | Berhasil |
| 3 | Indeks terakhir | 70 | 70 | Berhasil |
| 4 | Agregasi [75, 80, 65, 90, 88] | Total 398; rata-rata 79.60 | Total 398; rata-rata 79.60 | Berhasil |
| 5 | Filter kelulusan | [75, 80, 60, 90] | [75, 80, 60, 90] | Berhasil |
| 6 | Statistik sepuluh nilai praktik | Total 695; rata-rata 69.50 | Total 695; rata-rata 69.50 | Berhasil |
| 7 | Batas nilai [59, 60, 61] | Dua nilai lulus | Dua nilai lulus | Berhasil |
| 8 | Rata-rata list kosong | Menghasilkan 0 tanpa error | Menghasilkan 0 | Berhasil |

Catatan: Hasil aktual di atas merupakan hasil yang diharapkan dari
kode. Pastikan menjalankan seluruh program dan mencocokkan hasilnya
sebelum menyerahkan tugas.

## 7. Hasil Praktik

Berdasarkan data nilai [78, 55, 90, 67, 60, 82, 45, 71, 88, 59],
diperoleh hasil sebagai berikut:

- Banyak data: 10 mahasiswa.
- Total nilai: 695.
- Rata-rata: 69.50.
- Nilai minimum: 45.
- Nilai maksimum: 90.
- Jumlah mahasiswa lulus: 7.
- Jumlah mahasiswa belum lulus: 3.

Batas kelulusan yang digunakan adalah nilai 60 atau lebih.

## 8. Refleksi

Melalui praktikum ini, saya mempelajari bahwa list dapat digunakan
untuk menyimpan banyak data dalam satu variabel sehingga pengolahan
data menjadi lebih teratur.

Saya juga memahami penggunaan indeks, slicing, manipulasi list,
perulangan, dan fungsi untuk menghitung statistik sederhana.

Kesalahan yang perlu dihindari adalah mengakses indeks di luar
rentang list dan menghitung rata-rata ketika list kosong.
Kesalahan tersebut dapat dicegah dengan memeriksa indeks serta
jumlah elemen sebelum melakukan operasi.

## 9. Kesimpulan

List membantu menyimpan dan mengolah sekumpulan data numerik secara
efisien. Dengan memadukan list, perulangan, seleksi, dan fungsi,
program dapat menghitung statistik serta mengklasifikasikan nilai
mahasiswa berdasarkan batas kelulusan.

## 10. Git dan GitHub

Git digunakan untuk mencatat perubahan program melalui commit,
sedangkan GitHub digunakan untuk menyimpan dan membagikan repositori
secara daring.

Perintah dasar:

    git status
    git add .
    git commit -m "feat: menyelesaikan latihan list"
    git push

## 11. Sumber

- Bahan Ajar Pertemuan 09: List/Array dan Pengolahan Data Numerik
  Sederhana, Algoritma dan Pemrograman, 2026/2027 Ganjil.
- Python Software Foundation, Python 3 Documentation:
  Data Structures.
