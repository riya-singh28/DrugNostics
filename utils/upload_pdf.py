import streamlit as st
from pathlib import Path
import pandas as pd
import numpy as np
import os
import errno
import requests
import time

TOKEN = 987651234

def upload_file():
    uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")

    Submit = st.button(label='Submit')

    if Submit :
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
            url = f'http://34.125.142.75:8009/{TOKEN}/upload'
            file = {'file': open(save_path, 'rb')}
            resp = requests.post(url=url, files=file)
            st.success(f'File {uploaded_file.name} is successfully saved!')
            data = get_extracted_smiles()
            return data['smiles']

def get_extracted_smiles():
    r = requests.get(url = f'http://34.125.142.75:8009/{TOKEN}/extract')
    print("waiting")
    data = r.json()
    return data










