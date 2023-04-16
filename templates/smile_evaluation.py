import streamlit as st
import pandas as pd
from PIL import Image
from utils.upload_pdf import upload_file
from utils.smiles_to_feature import text_input
import requests

TOKEN = 987651234

def smile_evaluation():
    st.header('Smile Evaluation')
    st.subheader('About the datasets and model used')
    st.write('The Side Effect Resource (SIDER) is a database of marketed drugs and adverse drug reactions (ADR). The version of the SIDER dataset in DeepChem has grouped drug side effects into 27 system organ classes following MedDRA classifications measured for 1427 approved drugs.')
    st.write('The Delaney (ESOL) dataset a regression dataset containing structures and water solubility data for 1128 compounds. The dataset is widely used to validate machine learning models on estimating solubility directly from molecular structures (as encoded in SMILES strings).')
    smile = st.text_input("Enter the smiles")
    feature_list = ['Hepatobiliary disorders', 'Metabolism and nutrition disorders',
       'Product issues', 'Eye disorders', 'Investigations',
       'Musculoskeletal and connective tissue disorders',
       'Gastrointestinal disorders', 'Social circumstances',
       'Immune system disorders',
       'Reproductive system and breast disorders',
       'Neoplasms benign, malignant and unspecified (incl cysts and polyps)',
       'General disorders and administration site conditions',
       'Endocrine disorders', 'Surgical and medical procedures',
       'Vascular disorders', 'Blood and lymphatic system disorders',
       'Skin and subcutaneous tissue disorders',
       'Congenital, familial and genetic disorders',
       'Infections and infestations',
       'Respiratory, thoracic and mediastinal disorders',
       'Psychiatric disorders', 'Renal and urinary disorders',
       'Pregnancy, puerperium and perinatal conditions',
       'Ear and labyrinth disorders', 'Cardiac disorders',
       'Nervous system disorders',
       'Injury, poisoning and procedural complications']
    opt = st.multiselect("Select Features ", ('Hepatobiliary disorders', 'Metabolism and nutrition disorders',
       'Product issues', 'Eye disorders', 'Investigations',
       'Musculoskeletal and connective tissue disorders',
       'Gastrointestinal disorders', 'Social circumstances',
       'Immune system disorders',
       'Reproductive system and breast disorders',
       'Neoplasms benign, malignant and unspecified (incl cysts and polyps)',
       'General disorders and administration site conditions',
       'Endocrine disorders', 'Surgical and medical procedures',
       'Vascular disorders', 'Blood and lymphatic system disorders',
       'Skin and subcutaneous tissue disorders',
       'Congenital, familial and genetic disorders',
       'Infections and infestations',
       'Respiratory, thoracic and mediastinal disorders',
       'Psychiatric disorders', 'Renal and urinary disorders',
       'Pregnancy, puerperium and perinatal conditions',
       'Ear and labyrinth disorders', 'Cardiac disorders',
       'Nervous system disorders',
       'Injury, poisoning and procedural complications'))
    
    index = []
    for i in opt:
        ind = feature_list.index(i)
        index.append(ind)

    
    st.write("The available properties for prediction in SIDER dataset are:- Hepatobiliary disorders, Metabolism and nutrition disorders, Product issues, Eye disorders, Investigations, Musculoskeletal and connective tissue disorders, Gastrointestinal disorders, Social circumstances, Immune system disorders, Reproductive system and breast disorders, Neoplasms benign, malignant and unspecified (incl cysts and polyps), General disorders and administration site conditions, Psychiatric disorders, Pregnancy, puerperium and perinatal conditions, Cardiac disorders, Nervous system disorders, Injury, poisoning and procedural complications")
    
    Submit = st.button(label='Submit')
    if Submit:
        model_name = "SIDER_GCN"
        r = requests.get(url = f'http://34.125.142.75:8009/{TOKEN}/predict/{smile}/{model_name}')
        data = r.json()
        st.info(data['preds'])
