
import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import matplotlib.pyplot as plt



header=st.container()
dataset=st.container()
features =st.container()
model_training=st.container()





with header:
    st.title('Web Scraping & Analysis')
    st.text('Need to scrape data from goodreads.com')


with dataset:
    st.header('Scraping')
    st.text('Scraping the information of the first 1000 books using BeautifulSoup and requests')
    st.text('The data scrap from multiple pages')
    
data=pd.read_csv('C:/Users/Venati Himanth/OneDrive/Desktop/my/my_data.csv',sep='&')


with features:
    st.header('Pandas')
    st.subheader('Pandas converted the data into a DataFrame')
    if st.checkbox('Show Center Information data'):
        st.subheader('Center Information data')
        st.write(data)










with model_training:
    st.header('Time to Data Analysis!!!')
    





chart_select = st.sidebar.selectbox(
    label="select the chart type",
    options=['scatterplots','lineplots','Histogram','Boxplot']

)
