import streamlit as st
from pathlib import Path
import pandas as pd
import numpy as np
import os
import errno

def upload_file():
    uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")
    user_input = st.text_input("Input Smiles")

    st.info(uploaded_file)

    Submit = st.button(label='Submit')

    if Submit :
        st.markdown("**The file is sucessfully Uploaded.**")

    # Save uploaded file to 'F:/tmp' folder.
        save_folder = './temp'
        try:
            os.mkdir(save_folder)
        except OSError as e:
            if e.errno == errno.EEXIST:
                print('Directory not created.')
            else:
                raise
        save_path = Path(save_folder, uploaded_file.name)
        with open(save_path, mode='wb') as w:
            w.write(uploaded_file.getvalue())

        if save_path.exists():
            st.success(f'File {uploaded_file.name} is successfully saved!')
            st.info(os.getcwd())
            st.info(os.system("ls"))
            with open(save_path, "rb") as file:
                st.download_button("download", file, mime="application/pdf")






