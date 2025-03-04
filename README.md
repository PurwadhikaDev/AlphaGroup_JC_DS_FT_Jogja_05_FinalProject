# Bank Marketing Campaign Analysis

## Links
- [Dashboard](https://lookerstudio.google.com/reporting/3f25786a-fe18-41ea-9d61-16b640088ba4) 

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
Model ini hanya berlaku untuk rentang data berikut:
- **Age**: 17 hingga 98 tahun
- **Campaign**: 1 hingga 43 kali
- **Pdays**: 0 hingga 27 atau 999 (tidak dikontak)
- **Previous**: 0 hingga 7
- **Poutcome**: "failure", "nonexistent", "success"
- **Emp.var.rate**: -3.4 hingga 1.4
- **Cons.price.idx**: 92.201 hingga -26.9
- **Euribor3m**: 0.634 hingga 5.045
- **Nr.employed**: 4963.6 hingga 5228.1

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

## Deployment
### Tahapan Deployment
1. Simpan model dalam format `.pkl`.
2. Buat folder `Test_Model_ML` untuk menyimpan model dan file pendukung.
3. Buat `requirements.txt` untuk library yang dibutuhkan.
4. Buat folder `static/` dan `templates/` untuk file CSS dan HTML.
5. Jalankan aplikasi dengan Flask.

### Contoh Perintah
```bash
python CSV_Baca_py.py
```

### Proses Di Memasukan Test
1. Download data X_Test1
2. Masukan / Input lalu tekan tombol prediksi
3. Hasil Prediksi akan berbentuk CSV terdownload otomatis

### Dashboard Screenshot
![Dashboard_Halaman1.jpg](https://github.com/PurwadhikaDev/AlphaGroup_JC_DS_FT_Jogja_05_FinalProject/blob/main/Dashboard_Halaman1.jpg)


![Dashboard_Halaman2.jpg](https://github.com/PurwadhikaDev/AlphaGroup_JC_DS_FT_Jogja_05_FinalProject/blob/main/Dashboard_Halaman2.jpg)
