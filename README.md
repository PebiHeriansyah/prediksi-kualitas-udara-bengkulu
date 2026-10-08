# Prediksi Kualitas Udara Bengkulu

Repository ini berisi dua implementasi studi kasus yang berasal dari dua materi perkuliahan dan memiliki keterkaitan dengan rencana penelitian prediksi kualitas udara.

## Struktur Repository

```text
prediksi-kualitas-udara-bengkulu/
├── hpc-dan-kualitas-udara/
└── analisis-data-dan-ai/
```

## Studi Kasus 1 — HPC dan Kualitas Udara

Implementasi dari materi **"Bridging Global Infrastructure to Address Local Challenge in High Performance Computing"**.

Studi kasus mengangkat permasalahan kualitas udara sebagai contoh permasalahan lokal yang dapat diselesaikan dengan pendekatan komputasi dan pemodelan. Implementasi menggunakan **Random Forest** untuk memprediksi nilai **ISPU** berdasarkan data kualitas udara dan faktor meteorologi, serta menganalisis **feature importance** untuk melihat kontribusi masing-masing variabel.

📂 Folder: [`hpc-dan-kualitas-udara/`](hpc-dan-kualitas-udara/)

## Studi Kasus 2 — Analisis Data dan AI

Implementasi dari materi **"Make Sense of Data with Analysis and AI"**.

Studi kasus menekankan pentingnya **data understanding**, **data preparation**, dan **feature engineering** dalam membangun model prediktif. Fitur historis (**lag**) dibentuk dari nilai ISPU sebelumnya untuk digunakan sebagai input model **predictive analytics**. Model **Random Forest** digunakan untuk memperkirakan nilai ISPU pada periode berikutnya dan **evaluasi** dilakukan menggunakan MAE, RMSE, dan R².

📂 Folder: [`analisis-data-dan-ai/`](analisis-data-dan-ai/)

## Teknologi

- **Python**
- **Pandas** — manipulasi dan analisis data
- **NumPy** — komputasi numerik
- **Scikit-learn** — machine learning (Random Forest, evaluasi model)

## Dataset

Dataset yang digunakan pada repository ini merupakan **dataset sintetis/demo untuk keperluan pembelajaran**. Dataset ini **bukan** data resmi kualitas udara Provinsi Bengkulu.

Kolom dataset:

| Kolom | Keterangan |
|---|---|
| tanggal | Tanggal pengamatan |
| pm25 | Konsentrasi PM2.5 |
| pm10 | Konsentrasi PM10 |
| suhu | Temperatur |
| kelembapan | Kelembapan udara |
| curah_hujan | Curah hujan |
| kecepatan_angin | Kecepatan angin |
| ispu | Nilai ISPU |

## Menjalankan Project

### Studi Kasus 1 — HPC dan Kualitas Udara

```bash
cd hpc-dan-kualitas-udara
pip install -r requirements.txt
python prediksi_ispu_hpc.py
```

### Studi Kasus 2 — Analisis Data dan AI

```bash
cd analisis-data-dan-ai
pip install -r requirements.txt
python prediksi_ispu_lag.py
```

Hasil evaluasi masing-masing studi kasus akan disimpan pada `hasil/hasil_evaluasi.txt` di dalam folder yang bersangkutan.


## Catatan

- Implementasi ini dibuat sebagai studi kasus pembelajaran.
- Dataset yang digunakan adalah dataset sintetis sehingga hasil evaluasi tidak boleh dianggap sebagai hasil penelitian kualitas udara Provinsi Bengkulu.
- Jangan mengunggah dataset penelitian yang memiliki batasan publikasi.
