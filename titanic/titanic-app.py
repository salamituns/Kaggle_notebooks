import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier

header = st.beta_container()
dataset = st.beta_container()
features = st.beta_container()
model_training = st.beta_container()
sidebar = st.beta_container()

with sidebar:
    st.header('User Input Features')

with header:
    st.title('Titanic Prediction App')
    st.text('This app predicts the Survived Persons! in principle from the famous Titanic accident')

with dataset:
    st.header('Titanic dataset')
    st.text('Data obtained from the [Kaggle Data library](https://www.kaggle.com/c/titanic/data) by [Strive School](https://strive.school/)')

    titanic_test = pd.read_csv('test.csv')
    st.write(titanic_test.head())

with features:
    st.header('The features will be added soon')

with model_training:
    st.header('Watchout')
    st.text('please stay tuned')


