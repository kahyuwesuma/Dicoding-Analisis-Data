import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

URL_DATASET = 'https://raw.githubusercontent.com/kahyuwesuma/dicoding-dataset/main/day.csv'
df = pd.read_csv(URL_DATASET)

def display_analysis(analysis_choice):
    if analysis_choice == 'Pola Penjualan Berdasarkan Musim':
        display_season_analysis(df)
    elif analysis_choice == 'Distribusi Penjualan Hari Libur vs Hari Kerja':
        display_holiday_workday_analysis(df)
    elif analysis_choice == 'Hubungan antara Kondisi Cuaca dan Jumlah Penjualan':
        display_weather_analysis(df)

def display_season_analysis(df):
    st.header('Pola Penjualan Berdasarkan Musim')
    season_mapping = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
    df['season_name'] = df['season'].map(season_mapping)

    for season, season_name in season_mapping.items():
        season_data = df[df['season'] == season]
        st.subheader(season_name)
        st.line_chart(season_data.set_index('dteday')['cnt'])


def display_holiday_workday_analysis(df):
    st.header('Distribusi Penjualan Hari Libur vs Hari Kerja')

    holiday_data = df[df['holiday'] == 1]['cnt']
    workday_data = df[df['holiday'] == 0]['cnt']

    st.subheader('Hari Libur')
    st.write("Distribusi penjualan pada hari libur:")
    st.bar_chart(holiday_data)

    st.subheader('Hari Kerja')
    st.write("Distribusi penjualan pada hari kerja:")
    st.bar_chart(workday_data)

def display_weather_analysis(df):
    st.header('Hubungan antara Kondisi Cuaca dan Jumlah Penjualan')
    st.write("Kondisi cuaca: 1=Clear, 2=Mist, 3=Light Rain/Snow, 4=Heavy Rain/Snow")

    # Menampilkan scatter plot untuk hubungan antara kondisi cuaca dan jumlah penjualan
    st.subheader('Scatter Plot')
    st.write("Visualisasi hubungan antara Kondisi Cuaca dan Jumlah Penjualan")
    st.write("Kondisi Cuaca (weathersit) vs. Jumlah Penjualan (cnt)")
    st.write("")

    st.scatter_chart(df[['weathersit', 'cnt']])
