import streamlit as st
import os

st.set_page_config(
    page_title="Tomi Di Gennaro - certificates",
    page_icon="🤓",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.header("Data and Python diplomas")
# st.title()

folder = "udemy"
for img in os.listdir(folder):
    imgpath = os.path.join(folder, img)
    filename = img.replace(".jpg", "")
    st.divider()
    # st.subheader(filename)
    st.image(imgpath, use_column_width="auto")
