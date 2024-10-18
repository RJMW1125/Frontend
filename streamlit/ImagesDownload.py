import streamlit as st
import requests

def images_download_page():
    st.title("Download Image")

    # 從 Django 後端下載圖片
    response = requests.get("http://your-django-backend-url/api/download/example.png")

    if response.status_code == 200:
        # 提供下載按鈕
        st.download_button(
            label="Download Image",
            data=response.content,
            file_name="example.png",
            mime="image/png"
        )
    else:
        st.error(f"Failed to download image, status code: {response.status_code}")
