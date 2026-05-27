import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Prediksi Penyakit Jantung", page_icon="🫀")

model = joblib.load("model_jantung.joblib")

st.title("🫀 Prediksi Penyakit Jantung")
st.markdown("Masukkan data pasien untuk memprediksi risiko penyakit jantung.")

age = st.slider("Usia", 20, 80, 50)
sex = st.pills("Jenis Kelamin", ["Perempuan", "Laki-laki"], default="Laki-laki")
cp = st.selectbox("Tipe Nyeri Dada", [0, 1, 2, 3], help="0=tanpa nyeri, 1=ringan, 2=sedang, 3=berat")
trestbps = st.slider("Tekanan Darah Istirahat (mmHg)", 90, 200, 120)
chol = st.slider("Kolesterol (mg/dl)", 100, 600, 200)
fbs = st.pills("Gula Darah Puasa > 120 mg/dl?", ["Tidak", "Ya"], default="Tidak")
restecg = st.selectbox("Hasil EKG Istirahat", [0, 1, 2])
thalach = st.slider("Detak Jantung Maksimum", 70, 210, 150)
exang = st.pills("Angina saat Olahraga?", ["Tidak", "Ya"], default="Tidak")
oldpeak = st.slider("Depresi Segmen ST", 0.0, 6.0, 1.0, step=0.1)
slope = st.selectbox("Kemiringan Segmen ST", [0, 1, 2])
ca = st.selectbox("Jumlah Pembuluh Darah Tersumbat", [0, 1, 2, 3])
thal = st.selectbox("Tipe Thalassemia", [0, 1, 2, 3])

if st.button("Prediksi", type="primary"):
    data = pd.DataFrame([[
        age,
        1 if sex == "Laki-laki" else 0,
        cp, trestbps, chol,
        1 if fbs == "Ya" else 0,
        restecg, thalach,
        1 if exang == "Ya" else 0,
        oldpeak, slope, ca, thal
    ]], columns=["age","sex","cp","trestbps","chol","fbs","restecg","thalach","exang","oldpeak","slope","ca","thal"])

    hasil = model.predict(data)[0]
    probabilitas = max(model.predict_proba(data)[0])

    if hasil == 1:
        st.error(f"⚠️ Model memprediksi pasien **BERISIKO SAKIT JANTUNG** dengan keyakinan {probabilitas*100:.1f}%")
    else:
        st.success(f"✅ Model memprediksi pasien **SEHAT** dengan keyakinan {probabilitas*100:.1f}%")

    st.caption("⚠️ Hasil ini bukan diagnosis medis. Konsultasikan ke dokter untuk pemeriksaan lebih lanjut.")

st.divider()
st.caption("Dibuat dengan 🫀 oleh Deez")