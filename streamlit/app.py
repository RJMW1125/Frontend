import streamlit as st
from DataAnalysis import data_analysis_page
from ImagesDownload import images_download_page
from ImagesUpload import images_upload_page

# 功能選單
st.sidebar.title("Main Menu")
selection = st.sidebar.selectbox("Choose a feature", ["Data Analysis", "Upload Image", "Download Image"])


if selection == "Data Analysis":
    data_analysis_page()
elif selection == "Upload Image":
    images_upload_page()
elif selection == "Download Image":
    images_download_page()
