"""
STUDI KASUS: ANALISIS DATA DAN AI
Predictive analytics untuk memprediksi ISPU periode berikutnya.

Materi: Make Sense of Data with Analysis and AI

Fokus:
- Data understanding
- Data preparation
- Feature engineering dengan fitur lag
- Predictive analytics
- Random Forest
- Evaluasi MAE, RMSE, R2
- Pencegahan data leakage melalui chronological split

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

# 1. Data understanding: membaca dan melihat struktur data
data = pd.read_csv(DATA_PATH)

# 2. Data preparation: memastikan data tersusun kronologis
data["tanggal"] = pd.to_datetime(data["tanggal"])
data = data.sort_values("tanggal").reset_index(drop=True)

# 3. Feature engineering:
#    hanya memakai informasi yang tersedia sebelum target.
data["ispu_lag_1"] = data["ispu"].shift(1)
data["ispu_lag_2"] = data["ispu"].shift(2)
data["ispu_lag_3"] = data["ispu"].shift(3)

# 4. Target = ISPU pada periode berikutnya
data["target_ispu"] = data["ispu"].shift(-1)

# 5. Menghapus baris yang belum memiliki fitur/target lengkap
data = data.dropna().reset_index(drop=True)

FITUR = [
    "ispu_lag_1",
    "ispu_lag_2",
    "ispu_lag_3",
    "suhu",
    "kelembapan",
    "curah_hujan",
    "kecepatan_angin",
]

X = data[FITUR]
y = data["target_ispu"]

# 6. Chronological split untuk menghindari penggunaan informasi masa depan
batas = int(len(data) * 0.80)

X_train = X.iloc[:batas]
X_test = X.iloc[batas:]
y_train = y.iloc[:batas]
y_test = y.iloc[batas:]

# 7. Model Random Forest
model = RandomForestRegressor(
    n_estimators=200,
    random_state=42,
    n_jobs=-1
)

# 8. Training
model.fit(X_train, y_train)

# 9. Prediksi ISPU periode berikutnya
prediksi = model.predict(X_test)

# 10. Evaluasi
mae = mean_absolute_error(y_test, prediksi)
rmse = np.sqrt(mean_squared_error(y_test, prediksi))
r2 = r2_score(y_test, prediksi)

# 11. Feature importance
importance = pd.DataFrame({
    "fitur": FITUR,
    "importance": model.feature_importances_
}).sort_values("importance", ascending=False)

# 12. Simpan hasil
RESULT_PATH.parent.mkdir(exist_ok=True)

with open(RESULT_PATH, "w", encoding="utf-8") as f:
    f.write("STUDI KASUS: ANALISIS DATA DAN AI\n")
    f.write("Prediksi ISPU Periode Berikutnya Menggunakan Data Historis dan Faktor Meteorologi\n\n")
    f.write("DATASET: SINTETIS UNTUK DEMONSTRASI TUGAS\n\n")
    f.write("HASIL EVALUASI\n")
    f.write(f"MAE  : {mae:.4f}\n")
    f.write(f"RMSE : {rmse:.4f}\n")
    f.write(f"R2   : {r2:.4f}\n\n")
    f.write("FEATURE IMPORTANCE\n")
    f.write(importance.to_string(index=False))

print("=" * 55)
print("STUDI KASUS: ANALISIS DATA DAN AI")
print("=" * 55)
print(f"MAE  : {mae:.4f}")
print(f"RMSE : {rmse:.4f}")
print(f"R2   : {r2:.4f}")
print("\nFeature importance:")
print(importance.to_string(index=False))
print(f"\nHasil tersimpan: {RESULT_PATH}")
