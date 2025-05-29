# 🧠 LegalEase: Smarter Legal Document Summarizer

LegalEase is an AI-powered web application that helps users *upload large legal PDF files* and receive *structured summaries, clause highlights, and a **smart glossary* for simplified understanding. Built to make contracts easier to read, interpret, and reference — all in seconds.

🚀 Designed during a 48-hour hackathon with a focus on accessibility, legal insight, and responsible AI usage.

---

## 📌 Features

- 📄 *Upload PDF: Accepts files up to **200MB*.
- ✨ *Summarize: Uses **DistilBART*, a distilled version of BART, for fast and accurate legal summarization.
- 🔍 *Clause Extraction*: Identifies key clauses like Termination, Payment, Indemnity, Governing Law, etc.
- 📘 *Glossary Generator*: Explains the most repeated legal terms in plain English.
- 💡 *Highlighted Output*: Visually highlights clauses and summaries for better readability.
- 📥 *Download Summary*: Users can download the summarized version as a .txt file.
- ⚠ *Disclaimer*: Not a replacement for legal advice — meant for reference only.

---

## 🛠 Tech Stack

| Layer     | Tools Used                       |
|-----------|----------------------------------|
| Frontend  | [Streamlit](https://streamlit.io/) |
| Backend   | Python, Transformers (🤗 HuggingFace) |
| Models    | DistilBART, Regex for Clause Extraction |
| PDF Parser| PyMuPDF (fitz)               |
| Hosting   | Localhost (Streamlit) / deployable on GCP, Heroku, etc. |
| Optional  | MongoDB (for future storage & logging) |

---
---

## 📈 How It Works

1. 📤 *Upload* your legal document (PDF).
2. 🧠 *Summarizer* processes it chunk-by-chunk using DistilBART.
3. 📌 *Regex Engine* extracts important clauses.
4. 📘 *Glossary* identifies repeated legal terms and explains them.
5. 📄 *Download* the summary and review highlights inside the original document.

---

## 🎯 Use Cases

- 🧾 Contract Analysis
- 📚 Legal Education
- 🕵 Research Assistance
- 🧑‍⚖ Early-stage Legal Review

---

## 🚧 Limitations

- ❗ AI-based summaries may miss context — always consult a legal expert.
- 🧠 Currently supports English-language PDFs only.
- ⏱ Large documents (~200MB) may take longer processing time on CPU.

---

## 🤝 Contributing

Pull requests, suggestions, and improvements are welcome! This is a great base for legal AI, document analysis, or educational tools.

---

> ⚠ *Disclaimer*: This tool is meant for educational and reference purposes only and should not be considered a substitute for professional legal advice.