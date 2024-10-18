import streamlit as st
import requests

def images_upload_page():
    st.title("Upload Image")

    uploaded_file = st.file_uploader("Please upload an image", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        # 顯示圖片
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

        # 將圖片發送到 Django 後端
        files = {'file': uploaded_file.getvalue()}
        response = requests.post("http://your-django-backend-url/api/upload/", files=files)

        if response.status_code == 200:
            st.success("Image uploaded successfully")
        else:
            st.error(f"Failed to upload image, status code: {response.status_code}")
