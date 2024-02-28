import streamlit as st
from modules import analysis

def main():
    st.sidebar.header('Pilih Analisis')
    analysis_choice = st.sidebar.selectbox('Analisis yang Tersedia:', ['Pola Penjualan Berdasarkan Musim', 'Distribusi Penjualan Hari Libur vs Hari Kerja', 'Hubungan antara Kondisi Cuaca dan Jumlah Penjualan'])

    analysis.display_analysis(analysis_choice)

if __name__ == '__main__':
    main()
