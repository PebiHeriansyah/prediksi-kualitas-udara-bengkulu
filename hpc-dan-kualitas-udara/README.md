# HPC dan Kualitas Udara

## Deskripsi

Studi kasus ini merupakan implementasi dari materi **"Bridging Global Infrastructure to Address Local Challenge in High Performance Computing"**.

Implementasi mengambil contoh permasalahan lokal berupa prediksi kualitas udara menggunakan data kualitas udara dan faktor meteorologi.

Tujuan implementasi adalah menunjukkan bagaimana data, pemodelan, dan komputasi dapat digunakan untuk membantu menyelesaikan permasalahan kualitas udara.

## Kaitan dengan Materi

Materi membahas penggunaan **High Performance Computing (HPC)** untuk membantu menyelesaikan berbagai permasalahan nyata, antara lain:

- Prediksi banjir
- Pertanian
- Kesehatan
- Kualitas udara dan PM2.5

Konsep utama yang diangkat adalah **integrator**, yaitu menghubungkan:

> Masalah → Data → Model → Komputasi → Hasil → Informasi yang dapat digunakan

Dalam studi kasus ini, konsep tersebut disederhanakan menjadi:

> Data kualitas udara dan meteorologi → Preprocessing → Random Forest → Feature Importance → Prediksi ISPU → Evaluasi

## Studi Kasus

**Prediksi Kualitas Udara Berdasarkan Data Kualitas Udara dan Faktor Meteorologi**

**Tujuan:** Membangun contoh model prediksi ISPU menggunakan data kualitas udara dan faktor meteorologi.

## Dataset

Dataset yang digunakan merupakan **dataset DEMO/SINTETIS** untuk keperluan pembelajaran. Dataset ini **bukan** data resmi kualitas udara Provinsi Bengkulu.

| Variabel | Keterangan |
|---|---|
| tanggal | Tanggal pengamatan |
| pm25 | Konsentrasi PM2.5 |
| pm10 | Konsentrasi PM10 |
| suhu | Temperatur |
| kelembapan | Kelembapan udara |
| curah_hujan | Curah hujan |
| kecepatan_angin | Kecepatan angin |
| ispu | Nilai ISPU (target) |

## Metode

Proses yang dilakukan dalam implementasi:

1. **Membaca dataset** — memuat `data/data_kualitas_udara.csv`.
2. **Preprocessing** — mengubah kolom tanggal menjadi format tanggal dan membersihkan missing value.
3. **Pengurutan berdasarkan waktu** — memastikan data tersusun secara kronologis.
4. **Pemisahan data** — membagi data menjadi 80% training dan 20% testing berdasarkan urutan waktu.
5. **Random Forest** — melatih model `RandomForestRegressor` dengan `n_estimators=200`.
6. **Prediksi ISPU** — memprediksi nilai ISPU pada data testing.
7. **Feature importance** — melihat kontribusi masing-masing fitur terhadap prediksi.
8. **Evaluasi** — menghitung MAE, RMSE, dan R².

## Implementasi

File utama: `prediksi_ispu_hpc.py`

Cara menjalankan:

```bash
pip install -r requirements.txt
python prediksi_ispu_hpc.py
```

## Hasil

Hasil evaluasi disimpan pada `hasil/hasil_evaluasi.txt`.

Hasil yang dihasilkan merupakan **hasil demonstrasi menggunakan dataset sintetis** dan bukan hasil penelitian skripsi.

## Hubungan dengan Rencana Skripsi

Implementasi ini merupakan tahap awal yang berkaitan dengan rencana skripsi:

**"PEMODELAN PREDIKTIF KUALITAS UDARA MENGGUNAKAN RANDOM FOREST DAN ADAPTIVE NEURO-FUZZY INFERENCE SYSTEM DENGAN OPTIMASI PARTICLE SWARM OPTIMIZATION (Studi Kasus: Provinsi Bengkulu)"**

Dalam skripsi, proses akan dikembangkan menjadi:

> Data kualitas udara + data meteorologi → Preprocessing → Feature Engineering → Random Forest → Feature Selection → ANFIS → Optimasi PSO → Prediksi ISPU → Evaluasi

ANFIS dan PSO **belum diimplementasikan** dalam folder ini. Folder ini hanya mencakup tahap awal menggunakan Random Forest untuk prediksi dan feature importance.

## Catatan

Implementasi ini dibuat sebagai studi kasus pembelajaran. Dataset yang digunakan adalah dataset sintetis sehingga hasil evaluasi **tidak boleh** dianggap sebagai hasil penelitian kualitas udara Provinsi Bengkulu.
