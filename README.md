# Prediksi Kualitas Udara Bengkulu

Repository ini berisi implementasi dari berbagai pendekatan komputasi dan analisis data untuk memodelkan dan memprediksi kualitas udara.

## Struktur Repository

```text
prediksi-kualitas-udara-bengkulu/
├── hpc-dan-kualitas-udara/
└── analisis-data-dan-ai/
```

## HPC dan Kualitas Udara

Bagian ini mengangkat permasalahan kualitas udara sebagai contoh permasalahan lokal yang dapat diselesaikan dengan pendekatan komputasi kinerja tinggi (High Performance Computing). Implementasi menggunakan **Random Forest** untuk memprediksi nilai **ISPU** berdasarkan data kualitas udara dan faktor meteorologi, serta menganalisis **feature importance** untuk melihat kontribusi masing-masing variabel secara efisien.

📂 Folder: [`hpc-dan-kualitas-udara/`](hpc-dan-kualitas-udara/)

## Analisis Data dan AI

Bagian ini menekankan pentingnya **data understanding**, **data preparation**, dan **feature engineering** dalam membangun model prediktif untuk kualitas udara. Fitur historis (**lag**) dibentuk dari nilai ISPU sebelumnya untuk digunakan sebagai input model **predictive analytics**. Model **Random Forest** digunakan untuk memperkirakan nilai ISPU pada periode berikutnya dan **evaluasi** dilakukan menggunakan MAE, RMSE, dan R².

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

### HPC dan Kualitas Udara

```bash
cd hpc-dan-kualitas-udara
pip install -r requirements.txt
python prediksi_ispu_hpc.py
```

### Analisis Data dan AI

```bash
cd analisis-data-dan-ai
pip install -r requirements.txt
python prediksi_ispu_lag.py
```

Hasil evaluasi dari masing-masing pendekatan akan disimpan pada `hasil/hasil_evaluasi.txt` di dalam folder yang bersangkutan.


## Catatan

- Implementasi ini dibuat sebagai bentuk pembelajaran pemodelan prediktif.
- Dataset yang digunakan adalah dataset sintetis sehingga hasil evaluasi tidak boleh dianggap sebagai hasil penelitian observasi aktual kualitas udara Provinsi Bengkulu.
- Jangan mengunggah dataset penelitian yang memiliki batasan publikasi.
