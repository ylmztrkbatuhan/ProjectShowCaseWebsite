import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Ardit Sulce")
    content = """Hi I am ardit! I am a  python programmer, teacher, and founder of PythonHow. I graduated in 2013.
    I have worked with companies from various countries, such as center for conservation geography."""

    st.info(content)

content2 ="""Below you can find some of the apps I have built in Python. Feel free to contact me!"""

st.write(content2)