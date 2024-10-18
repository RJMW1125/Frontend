import streamlit as st
import requests
import pandas as pd

def data_analysis_page():
    st.title("Data Analysis")

    # 上傳資料集
    uploaded_file = st.file_uploader("Please upload a dataset (CSV)", type=["csv"])

    if uploaded_file is not None:
        # 將資料集發送到 Django 後端
        files = {'file': uploaded_file.getvalue()}
        response = requests.post("http://your-django-backend-url/api/upload_dataset/", files=files)

        if response.status_code == 200:
            st.success("Dataset uploaded successfully")
        else:
            st.error(f"Failed to upload dataset, status code: {response.status_code}")

        # 獲取分析結果
        analysis_response = requests.get("http://your-django-backend-url/api/analyze_dataset/")

        if analysis_response.status_code == 200:
            analysis_data = pd.DataFrame(analysis_response.json())
            st.write(analysis_data)
        else:
            st.error(f"Failed to fetch analysis results, status code: {analysis_response.status_code}")
