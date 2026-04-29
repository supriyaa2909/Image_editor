import streamlit as st
from PIL import Image
import cv2
import streamlit as st
from filters import *
from utils import *
st.title("🖼️ Image Editing App")
st.write("Upload an image and apply filters in real time.")

uploaded_file = st.file_uploader(
    "Choose an image", type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    original = pil_to_cv(image)

    st.sidebar.header("🎨 Apply Filters")

    blur = st.sidebar.slider("Blur", 1, 51, 1, step=2)
    sharpness = st.sidebar.slider("Sharpness", 0.0, 3.0, 1.0, 0.1)
    brightness = st.sidebar.slider("Brightness", -100, 100, 0)
    contrast = st.sidebar.slider("Contrast", 0.5, 3.0, 1.0, 0.1)

    grayscale = st.sidebar.checkbox("Grayscale")
    edge = st.sidebar.checkbox("Edge Detection")

    width = st.sidebar.slider("Width", 100, 2000, original.shape[1])
    height = st.sidebar.slider("Height", 100, 2000, original.shape[0])

    edited = original.copy()
    edited = resize_image(edited, width, height)
    edited = apply_blur(edited, blur)
    edited = apply_sharpness(edited, sharpness)
    edited = apply_brightness(edited, brightness)
    edited = apply_contrast(edited, contrast)

    if grayscale:
        edited = apply_grayscale(edited)

    if edge:
        edited = apply_edge_detection(edited, 100, 200)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original Image")
        st.image(image, use_container_width=True)

    with col2:
        st.subheader("Edited Image")
        st.image(cv_to_pil(edited), use_container_width=True)

    st.download_button(
        label="📥 Download Edited Image",
        data=image_to_bytes(edited),
        file_name="edited_image.png",
        mime="image/png"
    )
else:
    st.info("Please upload an image to begin.")