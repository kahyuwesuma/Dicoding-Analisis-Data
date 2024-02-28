import streamlit as st
import pandas as pd
import plotly.express as px

URL_DATASET = 'https://raw.githubusercontent.com/kahyuwesuma/dicoding-dataset/main/day.csv'
df = pd.read_csv(URL_DATASET)

def display_analysis(analysis_choice):
    if analysis_choice == 'Pola Penjualan Berdasarkan Musim':
        display_season_analysis()
    elif analysis_choice == 'Distribusi Penjualan Hari Libur vs Hari Kerja':
        display_holiday_workday_analysis()
    elif analysis_choice == 'Hubungan antara Kondisi Cuaca dan Jumlah Penjualan':
        display_weather_analysis()

def display_season_analysis():
    st.header('Pola Penjualan Berdasarkan Musim')
    season_mapping = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
    df['season_name'] = df['season'].map(season_mapping)
    fig_season = px.line(df, x='dteday', y='cnt', color='season_name', title='Pola Penjualan Berdasarkan Musim')
    fig_season.update_layout(xaxis_title='Tanggal', yaxis_title='Jumlah Penjualan')
    st.plotly_chart(fig_season)

def display_holiday_workday_analysis():
    st.header('Distribusi Penjualan Hari Libur vs Hari Kerja')
    fig_holiday_workday = px.box(df, x='holiday', y='cnt', color='holiday', title='Distribusi Penjualan pada Hari Libur vs Hari Kerja', labels={'holiday': 'Hari Libur', 'cnt': 'Jumlah Penjualan'})
    fig_holiday_workday.update_xaxes(type='category')
    fig_holiday_workday.update_traces(marker=dict(size=5))
    st.plotly_chart(fig_holiday_workday)

def display_weather_analysis():
    st.header('Hubungan antara Kondisi Cuaca dan Jumlah Penjualan')
    st.write("Kondisi cuaca: 1=Clear, 2=Mist, 3=Light Rain/Snow, 4=Heavy Rain/Snow")
    fig_weather = px.scatter(df, x='weathersit', y='cnt', title='Hubungan antara Kondisi Cuaca dan Jumlah Penjualan', labels={'weathersit': 'Kondisi Cuaca', 'cnt': 'Jumlah Penjualan'})
    fig_weather.update_traces(marker=dict(size=10, opacity=0.8))
    fig_weather.update_layout(xaxis=dict(tickmode='linear'))
    st.plotly_chart(fig_weather)
