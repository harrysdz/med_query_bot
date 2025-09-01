import streamlit as st
import requests

st.title("🩺 MedQueryBot")

query = st.text_input("Ask a medical research question")
if query:
    response = requests.post("http://localhost:8000/query", json={"question": query})
    st.write(response.json())