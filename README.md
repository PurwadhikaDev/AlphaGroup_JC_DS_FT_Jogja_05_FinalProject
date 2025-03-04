# Bank Marketing Campaign Analysis

## Links
- [Dashboard](https://lookerstudio.google.com/reporting/3f25786a-fe18-41ea-9d61-16b640088ba4)

  **Jika anda ingin mencoba langsung prediksinya, gass kuyy di link bawah ini:**
- [Streamlit](https://kelompokalpha.streamlit.app/)
  - Bisa Ditest menggunkan X_test1 **(Filenya bisa didownload di GitHub ini)**.

  **Jika ingin mencoba deploy manual memakai flask, ikuti langkah deploy yang berjudul Deployment Lokal diakhir pembahasan readme**
  
## Business Understanding

### Context
**Produk Deposito**  
Deposito berjangka adalah salah satu sumber pendanaan utama bagi bank dan merupakan opsi investasi yang stabil dan aman bagi nasabah. Nasabah menyimpan sejumlah uang untuk jangka waktu tertentu dan tidak dapat menariknya sebelum jatuh tempo. Bank meminjamkan uang tersebut ke nasabah lain dengan bunga lebih tinggi, mengambil margin dari selisih bunga (Net Interest Margin).

Telemarketing sering digunakan untuk menawarkan produk deposito kepada nasabah. Namun, konversi dari kegiatan ini seringkali rendah, sehingga diperlukan pendekatan yang lebih efektif.

### Problem Statement
Bank HAN di Portugal memiliki data kampanye telemarketing dari tahun 2008-2013. Konversi dari kegiatan telemarketing mereka hanya 11.8%, yang berarti sebagian besar panggilan berakhir dengan penolakan. Bank ingin meningkatkan efisiensi kampanye dengan mengidentifikasi nasabah potensial dan mengurangi biaya telemarketing.

### Goals
1. Memahami gambaran umum kegiatan telemarketing.
2. Mengidentifikasi nasabah potensial yang cenderung membuka deposito.
3. Mengoptimalkan anggaran marketing untuk meningkatkan profitabilitas.

### Analytical Approach
- **Variabel Target**:  
  - `0`: Nasabah tidak membuka deposito.  
  - `1`: Nasabah membuka deposito.  

- **Evaluation Metrics**:  
  - **True Positive (TP)**: Nasabah diprediksi membuka deposito dan benar-benar membuka.  
  - **False Positive (FP)**: Nasabah diprediksi membuka deposito, tetapi tidak membuka.  
  - **True Negative (TN)**: Nasabah diprediksi tidak membuka deposito dan benar tidak membuka.  
  - **False Negative (FN)**: Nasabah diprediksi tidak membuka deposito, tetapi ternyata membuka.  

- **Prioritas Metrik**: Recall untuk mengurangi False Negative (kehilangan nasabah potensial).

---

## Data Understanding
Dataset: [Bank Marketing Campaigns Dataset | Opening Deposit](https://archive.ics.uci.edu/ml/datasets/bank+marketing)  
Sumber: S. Moro, P. Cortez, dan P. Rita. *A Data-Driven Approach to Predict the Success of Bank Telemarketing*. Decision Support Systems, Elsevier, 62:22-31, June 2014.

### Variabel Input
| No  | Variabel          | Deskripsi |
|-----|-------------------|-----------|
| 1   | age               | Usia (numerik) |
| 2   | job               | Jenis pekerjaan (kategori) |
| 3   | marital           | Status pernikahan (kategori) |
| 4   | education         | Tingkat pendidikan (kategori) |
| 5   | default           | Apakah memiliki kredit macet? (kategori) |
| 6   | housing           | Apakah memiliki kredit rumah? (kategori) |
| 7   | loan              | Apakah memiliki pinjaman pribadi? (kategori) |
| 8   | contact           | Jenis komunikasi kontak (kategori) |
| 9   | month             | Bulan terakhir kontak dilakukan (kategori) |
| 10  | day_of_week       | Hari dalam seminggu terakhir kontak dilakukan (kategori) |
| 11  | duration          | Durasi kontak terakhir dalam detik (numerik) |
| 12  | campaign          | Jumlah kontak selama kampanye ini (numerik) |
| 13  | pdays             | Jumlah hari sejak terakhir kali klien dikontak (numerik) |
| 14  | previous          | Jumlah kontak sebelum kampanye ini (numerik) |
| 15  | poutcome          | Hasil kampanye pemasaran sebelumnya (kategori) |

### Variabel Sosial & Ekonomi
| No  | Variabel          | Deskripsi |
|-----|-------------------|-----------|
| 16  | emp.var.rate      | Tingkat variasi pekerjaan (numerik) |
| 17  | cons.price.idx    | Indeks harga konsumen (numerik) |
| 18  | cons.conf.idx     | Indeks kepercayaan konsumen (numerik) |
| 19  | euribor3m         | Suku bunga Euribor 3 bulan (numerik) |
| 20  | nr.employed       | Jumlah karyawan (numerik) |

### Variabel Output (Target)
| No  | Variabel | Deskripsi |
|-----|----------|-----------|
| 21  | y        | Apakah klien berlangganan deposito? (biner: "yes", "no") |

---

## Exploratory Data Analysis (EDA)
Analisis lengkap tersedia di notebook.

---

## Preprocessing
Tahapan preprocessing meliputi:
1. Remove Data Duplication
2. Fill Missing Values
3. Encoding
4. Scaling
5. Oversampling

---

## Methodology (Modelling)
Analisis lengkap tersedia di notebook.

---

## Model Limitation
Model ini hanya berlaku pada rentang data yang digunakan dalam pemodelan ini, yaitu:

| Variabel          | Rentang / Kategori |
|------------------|------------------|
| **Age** | 17 hingga 98 tahun |
| **Age Group** | 15-19, 20-24, 25-29, 30-34, 35-39, 40-44, 45-49, 50-54, 55-59, 60-64, 65-69, 70-74, 75-79, 80-84, 85 and more |
| **Campaign** | 1 hingga 43 kali |
| **Pdays** | 0 hingga 27 atau 999 = Tidak dikontak |
| **Previous** | 0, 1, 2, 3, 4, 5, 6, 7 |
| **Poutcome** | "failure", "nonexistent", "success" |
| **Campaign** | Integer (jumlah kontak selama kampanye) |
| **Anomali_cpp** | 0 = Normal, 1 = Anomali |
| **Emp.var.rate** | -3.4 hingga 1.4 |
| **Cons.price.idx** | 92.201 hingga -26.9 |
| **Cons.conf.idx** | -50.8 hingga 94.767 |
| **Euribor3m** | 0.634 hingga 5.045 |
| **Nr.employed** | 4963.6 hingga 5228.1 |
| **Job** | "admin.", "blue-collar", "entrepreneur", "housemaid", "management", "retired", "self-employed", "services", "student", "technician", "unemployed", "unknown" |
| **Marital** | "divorced", "married", "single", "unknown" |
| **Education** | "basic.4y", "basic.6y", "basic.9y", "high.school", "illiterate", "professional.course", "university.degree", "unknown" |
| **Housing** | "no", "yes", "unknown" |
| **Loan** | "no", "yes", "unknown" |
| **Contact** | "cellular", "telephone" |
| **Month** | "jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec" |
| **Day_of_week** | "mon", "tue", "wed", "thu", "fri" |


---

## Conclusion and Recommendation

### Kesimpulan
1. **Gambaran Umum Kampanye**: Fokus pada nasabah dengan karakteristik demografi dan riwayat interaksi yang potensial.
2. **Identifikasi Nasabah Potensial**: Model berhasil mengidentifikasi 919 nasabah potensial dari 6231 nasabah yang dihubungi, menghemat biaya telemarketing sebesar 35.3%.
3. **Peningkatan Profitabilitas**: Cost to profit ratio turun dari 8.85% menjadi 6.95%.

### Rekomendasi
1. **Waktu dan Frekuensi Kontak**: Fokus pada bulan Maret, April, September, Oktober, dan Desember. Prioritaskan hari Kamis.
2. **Segmentasi Nasabah**: Fokus pada usia muda (15-24 tahun) dan usia tua (di atas 60 tahun).
3. **Strategi Telemarketing**: Durasi panggilan optimal adalah 3-5 menit.
4. **Faktor Ekonomi**: Manfaatkan kondisi ekonomi seperti suku bunga tinggi untuk meningkatkan penawaran deposito.

---

## Deployment Lokal
1. Simpan Model Machine Learning
Setelah melatih model, simpan model dalam format .pkl menggunakan pickle (jangan joblib, karena format dictionary model yang disimpan akan berubah jadi array).
________________________________________
2. Buat Folder untuk Menyimpan Model
Buat folder baru di laptop dengan nama Test_Model_ML. Folder ini akan menyimpan model dan file lain yang dibutuhkan.
________________________________________
3. Buat requirements.txt
Di dalam folder Test_Model_ML, buat file requirements.txt **(Filenya bisa didownload di GitHub ini)** ini untuk menyimpan daftar library yang dibutuhkan agar bisa diunduh dengan sekali install.
________________________________________
4. Buat Folder static/ dan templates/
Masuk ke dalam folder Test_Model_ML, lalu buat dua folder tambahan:
•	static/ → Menyimpan file CSS, JavaScript, atau gambar.
•	templates/ → Menyimpan file HTML untuk tampilan antarmuka.
________________________________________
5. Simpan Model di Test_Model_ML
Pindahkan file model yang sudah disimpan (model.pkl) ke dalam folder Test_Model_ML **(Filenya bisa didownload di GitHub ini)**.
________________________________________
6. Buat File CSV_Baca_py.py untuk Membaca Model dan Menjalankan Flask
Buat file CSV_Baca_py.py di dalam folder Test_Model_ML. **(Filenya bisa didownload di GitHub ini)**.
________________________________________
7. Buat File HTML di Dalam templates/
Buat file index.html di dalam folder templates/. **(Filenya bisa didownload di GitHub ini)**.
________________________________________
8. Simpan Semua File dan Jalankan CSV_Baca_py.py
Buka terminal atau command prompt, lalu masuk ke folder Test_Model_ML dan jalankan:

```sh
python CSV_Baca_py.py
```

Jika ada error library yang belum terinstall, jalankan:

```sh
pip install -r requirements.txt
```
________________________________________
9. Tunggu Hingga Muncul IP Lokal dan Jalankan di Browser
Setelah program berjalan, akan muncul alamat seperti:

Running on http://127.0.0.1:5000/

Buka browser, lalu masukkan alamat tersebut untuk mengakses aplikasi.



### Proses Di Memasukan Test
1. Download data X_Test1
2. Masukan / Input lalu tekan tombol prediksi
3. Hasil Prediksi akan berbentuk CSV terdownload otomatis

### Dashboard Screenshot
![Dashboard_Halaman1.jpg](https://github.com/PurwadhikaDev/AlphaGroup_JC_DS_FT_Jogja_05_FinalProject/blob/main/Dashboard_Halaman1.jpg)


![Dashboard_Halaman2.jpg](https://github.com/PurwadhikaDev/AlphaGroup_JC_DS_FT_Jogja_05_FinalProject/blob/main/Dashboard_Halaman2.jpg)
