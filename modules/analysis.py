import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

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

    st.header('Pola Penjualan Berdasarkan Musim')

    season_names = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}

    df['season_name'] = df['season'].map(season_names)

    sales_by_season = df.groupby('season_name')['cnt'].sum().reset_index()

    fig = px.bar(sales_by_season, x='season_name', y='cnt', title='Total Penjualan Berdasarkan Musim')
    fig.update_xaxes(title='Musim')
    fig.update_yaxes(title='Total Penjualan')
    st.plotly_chart(fig)


def display_holiday_workday_analysis(df):
    st.header('Distribusi Penjualan Hari Libur vs Hari Kerja')

    holiday_data = df[df['holiday'] == 1]['cnt']
    workday_data = df[df['holiday'] == 0]['cnt']

    fig = px.histogram(df, x='cnt', color='holiday', nbins=20, histnorm='probability density', 
                       title='Distribusi Penjualan Hari Libur vs Hari Kerja', 
                       labels={'cnt': 'Jumlah Penjualan', 'holiday': 'Hari Libur'})

    fig.update_traces(name=['Hari Libur', 'Hari Kerja'])  # Menambahkan label yang jelas pada legend
    fig.update_layout(barmode='overlay')
    st.plotly_chart(fig)
    
def display_weather_analysis(df):
    st.header('Hubungan antara Kondisi Cuaca dan Jumlah Penjualan')

    weather_categories = {1: 'Clear', 2: 'Mist', 3: 'Light Rain/Snow'}

    df['weather_condition'] = df['weathersit'].map(weather_categories)

    sales_by_weather = df.groupby('weather_condition')['cnt'].sum().reset_index()

    st.subheader('Jumlah Penjualan Berdasarkan Kondisi Cuaca')
    st.write("Visualisasi hubungan antara Kondisi Cuaca dan Jumlah Penjualan")

    st.bar_chart(sales_by_weather.set_index('weather_condition'))
