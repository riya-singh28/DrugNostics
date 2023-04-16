import streamlit as st
from pathlib import Path
import pandas as pd
import numpy as np
import os
import errno
import requests
import hydralit_components as hc
import time

TOKEN = 987651234

def upload_file():
    uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")
    # user_input = st.text_input("Input Smiles")

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
            url = f'http://34.125.142.75:8000/{TOKEN}/upload'
            file = {'file': open(save_path, 'rb')}
            resp = requests.post(url=url, files=file)
            st.success(f'File {uploaded_file.name} is successfully saved!')
            get_extracted_smiles()

def get_extracted_smiles():
    # a dedicated single loader 
    # with hc.HyLoader('Now doing loading',hc.Loaders.pulse_bars,):
    #     time.sleep(5)

    # for 3 loaders from the standard loader group
    with hc.HyLoader('Now doing loading',hc.Loaders.standard_loaders,index=[3,0,5]):
        time.sleep(5)

    # for 1 (index=5) from the standard loader group
    # with hc.HyLoader('Now doing loading',hc.Loaders.standard_loaders,index=5):
    #     time.sleep(5)

    # for 4 replications of the same loader (index=2) from the standard loader group
    # with hc.HyLoader('Now doing loading',hc.Loaders.standard_loaders,index=[2,2,2,2]):
    #     time.sleep(5)
    r = requests.get(url = f'http://34.125.142.75:8000/{TOKEN}/extract')
    data = r.json()
    print(data)










