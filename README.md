# 🫀 Prediksi Penyakit Jantung

Proyek machine learning untuk memprediksi risiko penyakit jantung pada pasien berdasarkan data hasil pemeriksaan medis. Menggunakan dataset publik **Heart Disease Cleveland UCI** dari Kaggle.

## 📋 Deskripsi

Model ini mengklasifikasikan apakah seorang pasien **berisiko menderita penyakit jantung atau tidak** berdasarkan 13 fitur medis. Menggunakan algoritma **Random Forest** dengan hyperparameter tuning via GridSearchCV untuk memaksimalkan Recall — metrik yang paling krusial di konteks medis.

> ⚠️ **Disclaimer:** Aplikasi ini bukan alat diagnosis medis. Hasil prediksi tidak menggantikan pemeriksaan dan diagnosis dari tenaga medis profesional.

## 🗂️ Struktur Folder

```
prediksi_jantung/
│
├── venv/                        ← virtual environment
├── notebook.ipynb               ← notebook training & evaluasi model
├── app.py                       ← aplikasi web Streamlit
├── model_jantung.joblib         ← model yang sudah dilatih
├── heart_cleveland_upload.csv   ← dataset
└── requirements.txt             ← daftar library
```

## 📊 Dataset

- **Sumber:** [Heart Disease Cleveland UCI - Kaggle](https://www.kaggle.com/datasets/cherngs/heart-disease-cleveland-uci)
- **297 data** pasien, **13 fitur** input
- **Target:** `condition` → 0 = Sehat (160) / 1 = Sakit (137)

| Fitur | Keterangan |
|---|---|
| `age` | Usia pasien |
| `sex` | Jenis kelamin (1=pria, 0=wanita) |
| `cp` | Tipe nyeri dada (0–3) |
| `trestbps` | Tekanan darah istirahat (mmHg) |
| `chol` | Kolesterol serum (mg/dl) |
| `fbs` | Gula darah puasa > 120 mg/dl |
| `restecg` | Hasil EKG istirahat (0–2) |
| `thalach` | Detak jantung maksimum saat olahraga |
| `exang` | Angina saat olahraga |
| `oldpeak` | Depresi segmen ST |
| `slope` | Kemiringan segmen ST (0–2) |
| `ca` | Jumlah pembuluh darah utama tersumbat (0–3) |
| `thal` | Tipe thalassemia (0–3) |

## 🧠 Model

- **Algoritma:** Random Forest Classifier
- **Preprocessing:** StandardScaler (semua fitur numerik)
- **Tuning:** GridSearchCV dengan `scoring="recall"` dan `cv=5`
- **Parameter terbaik:** `n_estimators=50`, `max_depth=None`, `min_samples_split=2`

### Performa Model

| Metrik | Sehat | Sakit |
|---|---|---|
| Precision | 0.77 | 0.70 |
| Recall | 0.72 | 0.75 |
| F1-Score | 0.74 | 0.72 |
| **Accuracy** | | **73%** |

### Feature Importance (Top 5)
1. `thalach` — Detak jantung maksimum (0.148)
2. `thal` — Tipe thalassemia (0.122)
3. `ca` — Jumlah pembuluh tersumbat (0.110)
4. `cp` — Tipe nyeri dada (0.098)
5. `age` — Usia (0.096)

## 🚀 Cara Menjalankan

### 1. Clone & Masuk Folder
```bash
git clone https://github.com/AndhikaNH/prediksi-jantung.git
cd prediksi-jantung
```

### 2. Buat & Aktifkan Virtual Environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install Library
```bash
pip install -r requirements.txt
```

### 4. Jalankan Aplikasi
```bash
streamlit run app.py
```

Buka browser di `http://localhost:8501`

## 📦 Requirements

```
pandas
scikit-learn
joblib
streamlit
```

## 📌 Catatan Penggunaan Aplikasi

Data input yang dibutuhkan berasal dari **hasil pemeriksaan medis** (lab, EKG, tes treadmill). Aplikasi ini dirancang untuk digunakan oleh tenaga medis yang sudah memiliki data hasil pemeriksaan pasien — bukan untuk self-diagnose.

## 👤 Author

Dibuat dengan 🤓 oleh **D**
