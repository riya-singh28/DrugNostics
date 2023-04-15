import streamlit as st
from PIL import Image
from utils.upload_pdf import upload_file
from utils.smiles_to_feature import text_input

def home_page():
    st.header("DrugNostics")
    image = Image.open('data/image.jpg')
    st.image(image)
    st.subheader("About Us")
    st.write("Welcome to DrugNostics. Our web app uses the latest in cheminformatics and machine learning to help researchers discover new drugs faster. By analyzing the chemical structure of existing drugs, we can generate a list of similar drug candidates. We also analyze patent data to identify new chemical structures that could be used for drug development. Our user-friendly tool is accessible to researchers from various backgrounds and has the potential to revolutionize the drug research field.")
    opt = st.radio("Do you have a smile already? ", ('Yes', 'No I have a pdf containing some chemical structures'))

    if opt == 'Yes':
        text_input()
    else:
        upload_file()


    st.subheader("Authors")
    st.write("Riya Singh, EC Engg, National Institute of Technology Karnataka, India")
    st.write("Aryan Amit Barsainyan, Mechanical Engg, National Institute of Technology Karnataka, India")