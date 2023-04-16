import streamlit as st
from pathlib import Path
import pandas as pd
import numpy as np

def text_input():
    text_input = st.text_input("Enter the smiles")
    Submit = st.button(label='Submit')
    if Submit:
        return text_input
