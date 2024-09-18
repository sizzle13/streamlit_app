
import streamlit as st
import plotly.express as px
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("car_price_prediction.csv", encoding="utf-8")

def main_page(): # app_1.py
    st.title("Car Price Prediction dataset")
    dff = df.head(5)
    st.dataframe(dff)
    col_1, col_2 = st.columns(2)
    with col_1:
        st.header("Numeric Columns Description")
        dff = df.describe()
        st.dataframe(dff)
    with col_2:
        st.header("Categorical Columns Description")
        dff = df.describe(include="O")
        st.dataframe(dff)

def first_page(): 
    st.title("Please enter car features you want to predict it's price: ")
    value = st.slider(min_value=0, max_value=16, label='Cylinders') 
    value_2 = st.slider(min_value=0, max_value=16, label='Airbags') 
    value_3 = st.select_slider(label="Drive Wheels", options=["Front", "4X4", "Rear"]) 
    value_4 = st.checkbox(label="Leather Interior") 
    value_5 = st.radio(label="Production Year" , options=['Nineties', "Early 2000s", "2000s"]) 
    value_6 = st.selectbox(label="Fuel Type", options=['Hybird', "Petrol", "Diesel", "LPG", "CNG", "Hydrogen", "Plug-in Hybrid"])
    value_7 = st.selectbox(label="Gear Box Type", options=['Automatic', "Manual", "Variator", "Tiptronic"])
    num_1 = st.number_input(label="Mileage")
    num_2 = st.number_input(label="Engine_volume")
    text_1 = st.text_input(label="Car Model", max_chars=1000, type="default")
    text_2 = st.text_input(label="Car Manufacturer", max_chars=1000, type="default")
    submit = st.button(label="Submit") 
    if submit:
        print(value)
        print(value_2)
        print(value_3)
        print(value_4)
        print(value_5)
        print(value_6)
        print(value_7)
        print(num_1)
        print(num_2)
        print(text_1)
        print(text_2)


def second_page(): 
    st.title("Univariate Analysis ")
    col_1, col_2 = st.columns(2)
    with col_1:
        fig = plt.figure(figsize=(5, 5))
        sns.histplot(df['Cylinders'], kde=True)
        st.pyplot(fig)
        fig2 = plt.figure(figsize=(5, 5))
        sns.histplot(df['Airbags'], kde=True)
        st.pyplot(fig2)
        fig3 = plt.figure(figsize=(5, 5))
        sns.histplot(df['Prod. year'], kde=True)
        st.pyplot(fig3)
        
    with col_2:
        fig5 = plt.figure(figsize=(5, 5))
        sns.countplot(x=df['Gear box type'])
        st.pyplot(fig5)
        fig6 = plt.figure(figsize=(5, 5))
        sns.countplot(x=df['Fuel type'])
        st.pyplot(fig6)
        fig7 = plt.figure(figsize=(10, 5))
        sns.countplot(x=df['Drive wheels'])
        st.pyplot(fig7)
        fig8 = plt.figure(figsize=(10, 5))
        sns.countplot(x=df['Category'])
        st.pyplot(fig8)

def third_page():
    st.title("Bivariate Analysis")
    st.subheader("How does price differ based on drive wheels and right/left wheel?") 
    fig = plt.figure(figsize=(5, 5))
    sns.barplot(x=df['Drive wheels'], y=df['Price'], hue=df['Wheel'], estimator=np.median)
    plt.ylim((0, 1000000))
    st.pyplot(fig)
    st.subheader("What is the effect of car color on price?")
    fig1 = plt.figure(figsize=(10, 5))
    sns.boxplot(df, x=df['Color'], y=df['Price'])
    plt.ylim((0, 1000000))
    st.pyplot(fig1)
    st.subheader("Distrubution of car prices based on gear box type and fuel type")
    fig2 = plt.figure(figsize=(10, 5))
    sns.boxplot(df, x=df['Gear box type'], y=df['Price'], hue=df['Fuel type'])
    plt.ylim((0, 1000000))
    st.pyplot(fig2)
    st.subheader("What is the average car pricess across the most 50 frequent car models?")
    fig3 = plt.figure(figsize = (15, 10))
    dff = df.groupby(['Model'])[['Price']].median().reset_index().sort_values(by = 'Price', ascending=False).head(10)
    sns.barplot(dff, y =dff['Price'], x = dff['Model'])
    st.pyplot(fig3)


page = st.sidebar.selectbox(label="choose a page", options=["main page", "Page 1", "Page 2", "Page 3"])
mapper_name_fn = {"main page":main_page, "Page 1":first_page, "Page 2":second_page, "Page 3":third_page}
mapper_name_fn[page]()
