import streamlit as st
from pathlib import Path
import pandas as pd
import numpy as np
from templates.login import login
from templates.signup import signup
from templates.home_page import home_page

# DB Management
import sqlite3
conn = sqlite3.connect('data.db', check_same_thread=False)
c = conn.cursor()
# DB  Functions


page_names_to_funcs = ['Main Page', 'Login', 'Sign-up']

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs)

if selected_page == 'Main Page':
    home_page()

elif selected_page == 'Login':
    a = login(c)

elif selected_page == 'Sign-up':
    a = signup(c, conn)

