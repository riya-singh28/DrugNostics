import streamlit as st
from pathlib import Path
import pandas as pd
import numpy as np

lst = []

def text_input():
    text_input = st.text_input("Enter the smiles")
    Submit = st.button(label='Submit')
    if Submit:
        display_smiles([text_input])

@st.cache_data  
def display_smiles(smiles_list):
    # n = st.number_input("Enter number of elements : ", min_value=1, max_value=10, value=5, step=1)
    lst.extend(smiles_list)
    df = pd.DataFrame(lst)
    st.dataframe(df)
