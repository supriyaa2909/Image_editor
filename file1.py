import streamlit as st
import cv2
st.title("Machine Learning")
st.write("Hello World")
st.write("Deep Learning")
#a=st.number_input("Enter a number")
#st.text(a)
#st.image("Imagepre.png")

img=cv2.imread("Imagepre.png")

st.image(img)
st.write("Resize it")
height=st.slider("select the height",100,500)
width=st.slider("select the width",100,500)
img1=cv2.resize(img,(width,height))
st.image(img1)