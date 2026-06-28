import streamlit as st
from dotenv import load_dotenv
import os

from pipeline import run_pipeline
from ui import display_dashboard

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

st.set_page_config(
    page_title="Deal Analyzer V3",
    layout="wide"
)

st.title("📄 Deal Analyzer V3")

uploaded_file = st.file_uploader(
    "Upload Contract",
    type=["pdf"]
)

if uploaded_file:

    st.success("PDF Uploaded Successfully!")

    if st.button("Analyze Contract"):

        with st.spinner("Analyzing Contract..."):

            answer = run_pipeline(
                uploaded_file,
                api_key
            )

        display_dashboard(answer)