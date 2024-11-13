import streamlit as st
import os


st.set_page_config(
    page_title="Tomi Di Gennaro - Env eng",
    page_icon="🤓",
    layout="centered",
    initial_sidebar_state="expanded",
)


st.header("Environmental Engineering Diploma")

folder = "university"
for img in os.listdir(folder):
    imgpath = os.path.join(folder, img)
    filename = img.replace(".jpg", "")
    st.divider()
    st.image(imgpath, use_column_width="auto")

