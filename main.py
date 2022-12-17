import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/my_photo.jpeg", width=500)

with col2:
    st.title("Amanda Aye Chan Moe")
    content = """
    Hi I'm Amanda. I'm currently working as a consultant at Deloitte Singapore. I graduated in 2020 with a Master of Science in Information Systems from 
    Nanyang Technological University Singapore. I'm widly enthusiatic about Data Engineering.
    """
    st.info(content)

content2 = """
Below you can find my personal projects I have developed. Feel Free to contact me.
"""
st.write(content2)

col3, col4 = st.columns(2)
df = pd.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])