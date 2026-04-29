import streamlit as st

st.title("Image Editor")

if "uploaded_file" in st.session_state:
    st.image(st.session_state["uploaded_file"])
    st.write("Now you can edit your image!")
else:
    st.warning("Please upload an image first.")import streamlit as stst.title("Image Editor")if "uploaded_file" in st.session_state:    st.image(st.session_state["uploaded_file"])    st.write("Now you can edit your image!")else:    st.warning("Please upload an image first.")