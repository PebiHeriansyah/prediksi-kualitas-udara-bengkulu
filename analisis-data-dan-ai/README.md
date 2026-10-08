# Analisis Data dan AI

## Deskripsi

Studi kasus ini merupakan implementasi dari materi **"Make Sense of Data with Analysis and AI"**.

Fokus utama adalah bagaimana data dipahami, dipersiapkan, diolah, dan digunakan untuk membangun model **predictive analytics**.

Studi kasus menggunakan data historis kualitas udara dan faktor meteorologi untuk memperkirakan nilai ISPU pada periode berikutnya.

## Kaitan dengan Materi

Materi menekankan bahwa analisis data bukan hanya menjalankan algoritma, tetapi dimulai dari **pemahaman terhadap masalah dan data**. Proses analisis mencakup data understanding, data preparation, data quality, data cleaning, serta berbagai jenis analisis mulai dari descriptive, diagnostic, predictive, hingga prescriptive analytics.

Prinsip penting yang ditekankan:

> **"Garbage in, garbage out"** — kualitas data sangat berpengaruh terhadap hasil analisis.

Jika data yang masuk tidak berkualitas, maka hasil analisis dan prediksi juga tidak dapat diandalkan.

## Pertanyaan Analitik

> Berdasarkan data historis kualitas udara dan faktor meteorologi, berapa nilai ISPU yang diperkirakan pada periode berikutnya?

## Jenis Analisis

Studi kasus ini berfokus pada **Predictive Analytics** karena tujuan utamanya adalah memperkirakan nilai ISPU pada periode berikutnya berdasarkan data historis.

## Dataset

Dataset yang digunakan merupakan **dataset DEMO/SINTETIS** untuk keperluan pembelajaran. Dataset ini **bukan** data resmi kualitas udara Provinsi Bengkulu.

Variabel utama:

| Variabel | Keterangan |
|---|---|
| tanggal | Tanggal pengamatan |
| pm25 | Konsentrasi PM2.5 |
| pm10 | Konsentrasi PM10 |
| suhu | Temperatur |
| kelembapan | Kelembapan udara |
| curah_hujan | Curah hujan |
| kecepatan_angin | Kecepatan angin |
| ispu | Nilai ISPU |

## Data Preparation

Tahapan yang dilakukan:

1. **Membaca dataset** — memuat `data/data_kualitas_udara.csv`.
2. **Memeriksa data** — memahami struktur dan isi data.
3. **Mengubah format tanggal** — memastikan kolom tanggal dalam format datetime.
4. **Mengurutkan data berdasarkan waktu** — menyusun data secara kronologis.
5. **Membentuk fitur lag** — membuat fitur historis dari nilai ISPU sebelumnya.
6. **Menentukan target** — ISPU pada periode berikutnya (`ispu.shift(-1)`).
7. **Menghapus missing value** — menghilangkan baris yang tidak lengkap akibat proses lag dan shift.
8. **Membagi data** — 80% training dan 20% testing secara kronologis.

## Feature Engineering

Fitur historis yang dibentuk:

- **`ispu_lag_1`** — nilai ISPU satu periode sebelumnya.
- **`ispu_lag_2`** — nilai ISPU dua periode sebelumnya.
- **`ispu_lag_3`** — nilai ISPU tiga periode sebelumnya.

Fitur lag digunakan untuk memasukkan informasi historis ke dalam model sehingga model dapat mempelajari pola dari data masa lalu.

## Data Leakage

Karena data bersifat **time series**, pembagian training dan testing dilakukan berdasarkan urutan waktu. Data masa depan tidak boleh digunakan untuk membentuk informasi pada data masa lalu. Hal ini dilakukan untuk **mengurangi risiko data leakage**.

## Model

Model yang digunakan: **Random Forest Regressor**

Random Forest digunakan untuk membangun model prediksi sekaligus melihat **feature importance** yang menunjukkan kontribusi masing-masing fitur terhadap prediksi.

## Evaluasi

Metrik evaluasi yang digunakan:

| Metrik | Fungsi |
|---|---|
| **MAE** | Mengukur rata-rata besar kesalahan absolut antara nilai prediksi dan nilai aktual. |
| **RMSE** | Memberikan penalti lebih besar terhadap kesalahan yang besar dibandingkan MAE. |
| **R²** | Menunjukkan kemampuan model dalam menjelaskan variasi pada target. |

## Implementasi

File utama: `prediksi_ispu_lag.py`

Cara menjalankan:

```bash
pip install -r requirements.txt
python prediksi_ispu_lag.py
```

Hasil evaluasi disimpan di `hasil/hasil_evaluasi.txt`.

## Hubungan dengan Rencana Skripsi

Implementasi ini berkaitan dengan rencana skripsi:

**"PEMODELAN PREDIKTIF KUALITAS UDARA MENGGUNAKAN RANDOM FOREST DAN ADAPTIVE NEURO-FUZZY INFERENCE SYSTEM DENGAN OPTIMASI PARTICLE SWARM OPTIMIZATION (Studi Kasus: Provinsi Bengkulu)"**

Dalam penelitian skripsi, alur akan dikembangkan menjadi:

> Data historis kualitas udara dan meteorologi → Preprocessing → Feature Engineering → Random Forest → Feature Selection → ANFIS → Optimasi PSO → Prediksi ISPU → Evaluasi

Implementasi pada folder ini **belum merupakan implementasi penuh metode ANFIS-PSO**. Folder ini merupakan studi kasus awal yang menekankan pemahaman data, preprocessing, feature engineering, predictive analytics, dan evaluasi.

## Catatan

Dataset yang digunakan merupakan **dataset sintetis/demo**. Hasil model hanya digunakan untuk menunjukkan proses implementasi dan **tidak boleh** dianggap sebagai hasil penelitian sebenarnya.
