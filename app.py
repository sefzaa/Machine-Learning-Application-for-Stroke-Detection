import streamlit as st
import pandas as pd
import pickle
import numpy as np

st.title("Aplikasi Prediksi Stroke")

gender = st.selectbox("Apa Jenis Kelamin Anda?", ['Pria', 'Wanita'])
ever_married = st.selectbox("Apakah Anda Sudah Menikah?", ['Ya', 'Tidak'])
work_type = st.selectbox("Apa Pekerjaan Anda?", ['Wirausaha', 'Swasta', 'PNS', 'Anak-anak'])
Residence_type = st.selectbox("Bagaimana Status Permukiman Tempat Tinggal Anda?", ['Pedesaan', 'Perkotaan'])
smoking_status = st.selectbox("Apakah Anda Seorang Perokok?", ['Tidak Merokok', 'Tidak Diketahui', 'Pernah Merokok', 'Merokok'])
age = st.number_input("Berapa Umur Anda?")
hypertension = st.number_input("Apakah Anda Pernah Mengidap Hipertensi? Ketik 1 untuk ya, 0 untuk tidak")
heart_disease = st.number_input("Apakah Anda Punya Penyakit Hati? Ketik 1 untuk ya, 0 untuk tidak")
avg_glucose_level = st.number_input("Berapa Level Rata-Rata Gula Anda?")
bmi = st.number_input("Berapa Indeks Massa Tubuh Anda?")


model = pickle.load(open("model.pkl","rb"))

data_input = pd.DataFrame([[gender, ever_married, work_type, Residence_type, smoking_status,
                            age, hypertension, heart_disease, avg_glucose_level, bmi
]],
            columns=["gender","ever_married","work_type","Residence_type","smoking_status",
                     "age","hypertension","heart_disease","avg_glucose_level","bmi"
])


data_input.replace({"Pria":"Male","Wanita":"Female",
                    "Anak-anak":"children", "PNS":"Govt_job",
                    "Swasta":"Private", "Wirausaha":"Self-employed",
                    "Pedesaan":"Rural", "Perkotaan":"Urban",
                    "Merokok":"smokes", "Pernah Merokok":"formerly smoked", 
                    "Tidak Merokok":"never smoked", "Tidak Diketahui":"Unknown",
                    "Ya":"Yes","Tidak":"No"}, inplace=True)

hasil = model.predict(data_input)

if st.button('Submit'):
    result = model.predict(data_input)[0]
    if result == 1:
        st.text('Anda diprediksi mengidap penyakit stroke.')
    else:
        st.text('Anda diprediksi tidak mengidap penyakit stroke.')