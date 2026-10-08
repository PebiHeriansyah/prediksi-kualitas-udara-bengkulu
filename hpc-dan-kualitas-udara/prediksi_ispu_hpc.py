"""
STUDI KASUS: HPC DAN KUALITAS UDARA
Pemanfaatan komputasi untuk prediksi kualitas udara.

Materi: Bridging Global Infrastructure to Address Local Challenge
        in High Performance Computing

Fokus:
- Masalah lokal: kualitas udara
- Data kualitas udara + meteorologi
- Random Forest sebagai implementasi pemodelan awal
- Feature importance
- Evaluasi prediksi

Dataset yang digunakan pada repository ini adalah data SINTETIS
untuk demonstrasi tugas, bukan data resmi Provinsi Bengkulu.
"""

from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "data" / "data_kualitas_udara.csv"
RESULT_PATH = ROOT / "hasil" / "hasil_evaluasi.txt"

FITUR = [
    "pm25",
    "pm10",
    "suhu",
    "kelembapan",
    "curah_hujan",
    "kecepatan_angin",
]

# 1. Membaca data
data = pd.read_csv(DATA_PATH)

# 2. Menyiapkan urutan waktu
data["tanggal"] = pd.to_datetime(data["tanggal"])
data = data.sort_values("tanggal")

# 3. Memeriksa dan membersihkan data
data = data.dropna(subset=FITUR + ["ispu"])

X = data[FITUR]
y = data["ispu"]

# 4. Membagi data berdasarkan urutan waktu
#    Tidak menggunakan random split karena data memiliki dimensi waktu.
batas = int(len(data) * 0.80)

X_train = X.iloc[:batas]
X_test = X.iloc[batas:]
y_train = y.iloc[:batas]
y_test = y.iloc[batas:]

# 5. Membuat model Random Forest
model = RandomForestRegressor(
    n_estimators=200,
    random_state=42,
    n_jobs=-1
)

# 6. Training
model.fit(X_train, y_train)

# 7. Prediksi
prediksi = model.predict(X_test)

# 8. Evaluasi
mae = mean_absolute_error(y_test, prediksi)
rmse = np.sqrt(mean_squared_error(y_test, prediksi))
r2 = r2_score(y_test, prediksi)

# 9. Feature importance
importance = pd.DataFrame({
    "fitur": FITUR,
    "importance": model.feature_importances_
}).sort_values("importance", ascending=False)

# 10. Simpan hasil
RESULT_PATH.parent.mkdir(exist_ok=True)

with open(RESULT_PATH, "w", encoding="utf-8") as f:
    f.write("STUDI KASUS: HPC DAN KUALITAS UDARA\n")
    f.write("Prediksi Kualitas Udara Berdasarkan Data Kualitas Udara dan Faktor Meteorologi\n\n")
    f.write("DATASET: SINTETIS UNTUK DEMONSTRASI TUGAS\n\n")
    f.write("HASIL EVALUASI\n")
    f.write(f"MAE  : {mae:.4f}\n")
    f.write(f"RMSE : {rmse:.4f}\n")
    f.write(f"R2   : {r2:.4f}\n\n")
    f.write("FEATURE IMPORTANCE\n")
    f.write(importance.to_string(index=False))

print("=" * 55)
print("STUDI KASUS: HPC DAN KUALITAS UDARA")
print("=" * 55)
print(f"MAE  : {mae:.4f}")
print(f"RMSE : {rmse:.4f}")
print(f"R2   : {r2:.4f}")
print("\nFeature importance:")
print(importance.to_string(index=False))
print(f"\nHasil tersimpan: {RESULT_PATH}")
