import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv('data/day.csv')

# Judul Dashboard
st.title('Dashboard Analisis Data')

# Tampilkan dataset
st.write(data.head())

# Visualisasi 1: Penggunaan Sepeda Berdasarkan Musim
st.write("Penggunaan Sepeda Berdasarkan Musim")
fig1, ax1 = plt.subplots()
sns.boxplot(x='season', y='cnt', data=data, ax=ax1)
st.pyplot(fig1)

# Visualisasi 2: Penggunaan Sepeda: Hari Kerja vs Akhir Pekan
st.write("Penggunaan Sepeda: Hari Kerja vs Akhir Pekan")
fig2, ax2 = plt.subplots()
sns.boxplot(x='workingday', y='cnt', data=data, ax=ax2)
st.pyplot(fig2)

# Tambahkan visualisasi atau elemen lainnya di sini
