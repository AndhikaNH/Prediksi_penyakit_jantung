# 🍊 Klasifikasi Kualitas Jeruk

Proyek machine learning untuk memprediksi kualitas jeruk berdasarkan karakteristik fisik dan asal daerahnya. 

## 📋 Deskripsi

Model ini mengklasifikasikan kualitas jeruk ke dalam tiga kategori: **Bagus**, **Sedang**, dan **Jelek** berdasarkan 7 fitur input. Menggunakan algoritma **Logistic Regression** yang dibungkus dalam Scikit-learn Pipeline lengkap dengan preprocessing otomatis.

## 🗂️ Struktur Folder

```
belajar_klasifikasi_jeruk/
│
├── venv/                            ← virtual environment
├── Belajar Klasifikasi Jeruk.ipynb  ← notebook training model
├── app_streamlit.py                 ← aplikasi web Streamlit
├── model_klasifikasi_jeruk.joblib   ← model yang sudah dilatih
├── jeruk_balance_500.csv            ← dataset
└── requirements.txt                 ← daftar library
```

## 📊 Dataset

- **500 data** jeruk yang sudah di-balance antar kelas
- **7 fitur input:**

| Fitur | Tipe | Keterangan |
|---|---|---|
| `diameter` | Numerik | Ukuran diameter jeruk (cm) |
| `berat` | Numerik | Berat jeruk (gram) |
| `tebal_kulit` | Numerik | Tebal kulit jeruk (cm) |
| `kadar_gula` | Numerik | Kadar gula jeruk |
| `asal_daerah` | Kategorikal | Kalimantan / Jawa Tengah / Jawa Barat |
| `warna` | Ordinal | hijau → kuning → oranye |
| `musim_panen` | Kategorikal | kemarau / hujan |

- **Target:** `kualitas` → Bagus (168) / Sedang (166) / Jelek (166)

## 🧠 Model

- **Algoritma:** Logistic Regression
- **Pipeline:**
  - `StandardScaler` → fitur numerik
  - `OneHotEncoder` → fitur kategorikal (asal_daerah, musim_panen)
  - `OrdinalEncoder` → fitur ordinal (warna)
- **Akurasi:** 99% (data sintetis)

## 🚀 Cara Menjalankan

### 1. Clone & Masuk Folder
```bash
git clone https://github.com/AndhikaNH/klasifikasi-jeruk.git
cd klasifikasi-jeruk
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
streamlit run app_streamlit.py
```

Buka browser di `http://localhost:8501`

## 📦 Requirements

```
pandas
matplotlib
seaborn
scikit-learn
joblib
streamlit
```

## 📌 Catatan

> Dataset yang digunakan adalah data **sintetis** (dibuat secara simulasi), bukan data nyata dari kebun jeruk. Akurasi 99% yang dihasilkan mencerminkan pola data yang terlalu linear — tidak mencerminkan kompleksitas data dunia nyata.

## 👤 Author

Dibuat dengan 🤓 oleh **D**
