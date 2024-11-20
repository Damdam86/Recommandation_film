import streamlit as st

st.title("L'équipe projet")
st.write("L'équipe")

st.divider()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.header("Yosser")
    st.image("C:/Users/cohen/Desktop/Damien/Data Analyst/Projet 2/Yosser.png")

with col2:
    st.header("Vincent")
    st.image("C:/Users/cohen/Desktop/Damien/Data Analyst/Projet 2/Vincent.png")

with col3:
    st.header("Damien")
    st.image("C:/Users/cohen/Desktop/Damien/Data Analyst/Projet 2/Damien.png")

with col4:
    st.header("Fatma")
    st.image("C:/Users/cohen/Desktop/Damien/Data Analyst/Projet 2/Fatma.png")

