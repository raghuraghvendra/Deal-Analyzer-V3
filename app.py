import os

import streamlit as st
from dotenv import load_dotenv

from pipeline import run_pipeline
from ui import display_dashboard

# -----------------------------
# Load Environment Variables
# -----------------------------
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# -----------------------------
# Streamlit Configuration
# -----------------------------
st.set_page_config(
    page_title="Deal Analyzer V3",
    layout="wide"
)

st.title("📄 Enterprise AI Contract Intelligence Platform")

# -----------------------------
# API Key Validation
# -----------------------------
if not api_key:

    st.error(
        "❌ GEMINI_API_KEY not found.\n\n"
        "Please configure your .env file."
    )

    st.stop()

# -----------------------------
# File Upload
# -----------------------------
uploaded_file = st.file_uploader(
    "Upload Contract",
    type=["pdf"]
)

if uploaded_file:

    if uploaded_file.size > 10 * 1024 * 1024:

        st.error("❌ File size exceeds 10 MB.")

        st.stop()

    st.success("✅ PDF Uploaded Successfully!")

    if st.button("Analyze Contract"):

        try:

            with st.spinner("Analyzing Contract..."):

                answer = run_pipeline(
                    uploaded_file,
                    api_key
                )

            st.success("✅ Analysis Completed")

            display_dashboard(answer)

        except Exception as e:

            st.error("❌ Contract Analysis Failed")

            with st.expander("View Error Details"):

                st.code(str(e))