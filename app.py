import streamlit as st
from summarizer import summarize_text
from clause_extractor import extract_clauses, generate_glossary
from pdf_parser import extract_text_from_pdf

st.set_page_config(page_title="Legal Contract Summarizer", layout="wide")

st.title("📄 Legal Contract Summarizer & Clause Highlighter")
st.markdown("Upload a contract to get a plain English summary and clause highlights.")

uploaded_file = st.file_uploader("Choose a contract file (.pdf)", type=["pdf"])

if uploaded_file:
    file_bytes = uploaded_file.read()

    raw_text = extract_text_from_pdf(file_bytes)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📜 Original Contract")
        st.text_area("Original Text", raw_text, height=400)

    with col2:
        st.subheader("📝 Summary")
        summary = summarize_text(raw_text, model_key="distilbart")
        st.text_area("Summary", summary, height=400)
        

    clauses, highlighted_text = extract_clauses(raw_text)
    st.subheader("🔍 Highlighted Clauses")
    st.markdown(highlighted_text, unsafe_allow_html=True)

    st.subheader("📘 Glossary")
    glossary = generate_glossary()
    for term, explanation in glossary.items():
        st.markdown(f"**{term.title()}**: {explanation}")

    st.download_button("⬇ Download Summary", summary, file_name="summary.txt", mime="text/plain")
    st.markdown("---")
    st.caption("⚠️ This tool is a demo. Always consult a legal professional for critical contracts.")