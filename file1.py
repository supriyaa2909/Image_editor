import streamlit as st
import cv2
st.title("Image Editor")
st.write("Welcome! please upload image")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.session_state["uploaded_file"] = uploaded_file
    st.switch_page("pages/editor.py")

#height=st.slider("select the height",100,500)
#width=st.slider("select the width",100,500)

#img1=cv2.resize(img,(width,height))
#st.image(img1)