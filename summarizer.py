from transformers import pipeline
from textwrap import wrap
from functools import lru_cache
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


MODEL_PARAMS = {
    "pegasus": {"model": "nsi319/legal-pegasus", "max_length": 512},
    "bart": {"model": "facebook/bart-large-cnn", "max_length": 512},
    "t5": {"model": "t5-base", "max_length": 300},
    "distilbart": {"model": "sshleifer/distilbart-cnn-12-6", "max_length": 150}
}


@lru_cache(maxsize=3)
def get_summarizer(model_key):
    config = MODEL_PARAMS.get(model_key, MODEL_PARAMS["pegasus"])
    logger.info(f"Loading model: {config['model']}")
    return pipeline("summarization", model=config["model"])


def chunk_text(text, max_tokens=800):
    paragraphs = [p.strip() for p in text.split("\n") if p.strip()]
    chunks = []
    current_chunk = ""

    for para in paragraphs:
        if len(current_chunk.split()) + len(para.split()) < max_tokens:
            current_chunk += para + "\n"
        else:
            chunks.append(current_chunk.strip())
            current_chunk = para + "\n"

    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks


def summarize_chunk(chunk, model_key):
    try:
        summarizer = get_summarizer(model_key)
        config = MODEL_PARAMS.get(model_key, MODEL_PARAMS["pegasus"])
        summary = summarizer(
            chunk,
            max_length=config["max_length"],
            min_length=100,
            do_sample=False
        )
        return summary[0]["summary_text"]
    except Exception as e:
        logger.error(f"Error summarizing chunk: {e}")
        return "[Error summarizing this section]"


def format_summary(summary):
    lines = summary.replace("\n", " ").split(". ")
    formatted = []

    for line in lines:
        line = line.strip().capitalize()
        if not line:
            continue

       
        if "termination" in line.lower():
            formatted.append(f"**Termination Clause:** {line}")
        elif "dispute" in line.lower() or "arbitration" in line.lower():
            formatted.append(f"**Dispute Resolution:** {line}")
        elif "payment" in line.lower() or "payable" in line.lower():
            formatted.append(f"**Payment Terms:** {line}")
        elif "license" in line.lower() or "copyright" in line.lower():
            formatted.append(f"**Intellectual Property:** {line}")
        elif "governing law" in line.lower() or "jurisdiction" in line.lower():
            formatted.append(f"**Governing Law:** {line}")
        elif "non-discrimination" in line.lower():
            formatted.append(f"**Non-Discrimination Policy:** {line}")
        elif "agreement" in line.lower() and "entire" in line.lower():
            formatted.append(f"**Entire Agreement:** {line}")
        else:
            formatted.append(f"- {line}")

    return "\n\n".join(formatted)


def summarize_long_text(text, model_key):
    chunks = chunk_text(text)
    logger.info(f"Split into {len(chunks)} chunk(s)")

    summaries = [summarize_chunk(chunk, model_key) for chunk in chunks]

   
    seen = set()
    deduped = []
    for s in summaries:
        if s not in seen:
            deduped.append(s)
            seen.add(s)

    merged = " ".join(deduped)
    return format_summary(merged)


def summarize_text(text, model_key="pegasus"):
    word_count = len(text.split())
    logger.info(f"Text length: {word_count} words. Using model: {model_key}")

    if word_count < 400:
        raw = summarize_chunk(text, model_key)
        return format_summary(raw)
    else:
        return summarize_long_text(text, model_key)
