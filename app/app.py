import streamlit as st
from utils.analysis import analyze_text

st.set_page_config(page_title="Judge Insight", layout="wide")

st.title("🔍 Judge Insight")
st.write("Analyze judicial texts and get insights.")

text_input = st.text_area("Enter legal text:", height=300)

if st.button("Analyze"):
    if text_input.strip():
        result = analyze_text(text_input)
        st.json(result)
    else:
        st.warning("Please enter some text to analyze.")