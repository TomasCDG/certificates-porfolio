import streamlit as st
import os


st.set_page_config(
    page_title="Tomi Di Gennaro - Le Wagon",
    page_icon="🤓",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.header("Le wagon Bootcamp Diploma")
# st.title()

folder = "le_wagon"
for img in os.listdir(folder):
    imgpath = os.path.join(folder, img)
    filename = img.replace(".jpg", "")
    st.image(imgpath, use_column_width="auto")
