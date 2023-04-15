import streamlit as st
from pathlib import Path
import pandas as pd
import numpy as np

lst = []

def text_input():
    text_input = st.text_input("Enter the smiles")
    Submit = st.button(label='Submit')
    if Submit:
        display_smiles(text_input)

@st.cache_data  
def display_smiles(text_input):
    # n = st.number_input("Enter number of elements : ", min_value=1, max_value=10, value=5, step=1)
    lst.append(text_input)

    df = pd.DataFrame(lst)
    st.dataframe(df)

def select_smile():
    opt = st.radio(lst)
    

    

# @st.cache_data   
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data
