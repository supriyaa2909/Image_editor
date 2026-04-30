# app.py
import streamlit as st
import numpy as np
import cv2

st.set_page_config(page_title="Image Editor", page_icon="🖼️", layout="wide")
st.title("🖼️ Image Editor")

uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    st.sidebar.header("Apply Filters")

    blur = st.sidebar.slider("Blur", 1, 25, 1, step=2)
    sharpness = st.sidebar.slider("Sharpness", 0.0, 3.0, 1.0)
    brightness = st.sidebar.slider("Brightness", -100, 100, 0)
    contrast = st.sidebar.slider("Contrast", 0.5, 3.0, 1.0)
    edge = st.sidebar.checkbox("Edge Detect")
    gray = st.sidebar.checkbox("Grayscale")

    edited = img.copy()

    if blur > 1:
        edited = cv2.GaussianBlur(edited, (blur, blur), 0)

    edited = cv2.convertScaleAbs(edited, alpha=contrast, beta=brightness)

    if sharpness > 1:
        kernel = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]])
        edited = cv2.filter2D(edited, -1, kernel)

    if gray:
        edited = cv2.cvtColor(edited, cv2.COLOR_RGB2GRAY)

    if edge:
        if len(edited.shape) == 3:
            edited = cv2.cvtColor(edited, cv2.COLOR_RGB2GRAY)
        edited = cv2.Canny(edited, 100, 200)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original Image")
        st.image(img, use_container_width=True)

    with col2:
        st.subheader("Edited Image")
        st.image(edited, use_container_width=True)
    _, buffer = cv2.imencode('.png', cv2.cvtColor(edited, cv2.COLOR_RGB2BGR) if len(edited.shape) == 3 else edited)
    st.download_button(
        label="📥 Download Edited Image",
        data=buffer.tobytes(),
        file_name="edited_image.png",
        mime="image/png"
    )    
else:
    st.info("Please upload an image to start editing.")