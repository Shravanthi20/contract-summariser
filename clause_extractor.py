import re

CLAUSE_PATTERNS = {
    "termination": r"\btermination\b.*?(?:\.\s|\n|$)",
    "cancellation": r"\bcancell?ation\b.*?(?:\.\s|\n|$)",
    "payment": r"\b(?:payment|shall pay|due on|invoice|compensation|fee|amount of)\b.*?(?:\.\s|\n|$)",
    "deadline": r"\b(?:no later than|by [A-Z][a-z]+ \d{1,2}|within \d+ (?:days|weeks|months))\b.*?(?:\.\s|\n|$)",
    "auto_renewal": r"\bauto[- ]?renew(al)?\b.*?(?:\.\s|\n|$)",
    "dispute_resolution": r"\b(?:dispute resolution|arbitration|mediation|resolve.*?dispute)\b.*?(?:\.\s|\n|$)",
    "governing_law": r"\b(?:governing law|jurisdiction of|under the laws of)\b.*?(?:\.\s|\n|$)",
    "confidentiality": r"\b(?:confidential information|non-disclosure|keep confidential|NDA)\b.*?(?:\.\s|\n|$)",
    "indemnity": r"\bindemnif(y|ication|ies|ied)\b.*?(?:\.\s|\n|$)",
    "intellectual_property": r"\b(intellectual property|IP rights|copyright|trademark|ownership)\b.*?(?:\.\s|\n|$)",
    "force_majeure": r"\b(force majeure|act of god|unforeseen circumstance)\b.*?(?:\.\s|\n|$)",
    "assignment": r"\bassign(?:ment)?\b.*?(?:\.\s|\n|$)",
    "liability": r"\b(limit(?:ation)? of liability|liable|liabilities|shall not be liable)\b.*?(?:\.\s|\n|$)",
    "warranty": r"\b(warranty|warranties|guarantee|as is|disclaimer)\b.*?(?:\.\s|\n|$)",
    "notice": r"\b(notice period|required notice|written notice|give notice)\b.*?(?:\.\s|\n|$)",
    "non_compete": r"\b(non-?compete|non-?solicit|restrictive covenant)\b.*?(?:\.\s|\n|$)",
    "severability": r"\bseverability\b.*?(?:\.\s|\n|$)",
    "entire_agreement": r"\b(entire agreement|whole agreement|entire understanding)\b.*?(?:\.\s|\n|$)"
}

def extract_clauses(text):
    """
    Extract legal clauses from the text using predefined regex patterns.
    Returns a list of clause matches and the annotated (highlighted) text.
    """
    matches = []
    for label, pattern in CLAUSE_PATTERNS.items():
        for match in re.finditer(pattern, text, flags=re.IGNORECASE):
            matches.append({
                "type": label,
                "text": match.group().strip(),
                "start": match.start(),
                "end": match.end()
            })

    highlighted = highlight_clauses(text, matches)
    return matches, highlighted


def highlight_clauses(text, matches):
    """
    Highlight extracted clauses in the text using <mark><b>...</b></mark> HTML tags.
    Returns the HTML-safe version of the annotated text.
    """
    matches = sorted(matches, key=lambda x: x["start"])
    result = ""
    last_end = 0

    for m in matches:
        result += text[last_end:m["start"]]
        result += f"<mark><b>{text[m['start']:m['end']]}</b></mark>"
        last_end = m["end"]
    result += text[last_end:]
    return result


def generate_glossary():
    """
    Glossary of key legal terms used in clause identification.
    """
    return {
        "arbitration": "A legal technique for resolving disputes outside courts.",
        "termination": "The legal end of a contract.",
        "remuneration": "Payment received for work or services.",
        "indemnity": "A contractual obligation to compensate for loss or damage.",
        "force majeure": "A clause that frees parties from obligation due to extraordinary events.",
        "confidentiality": "Requirement to keep certain information private.",
        "non-compete": "Restriction preventing a party from entering competition.",
        "governing law": "The legal jurisdiction that will oversee contract enforcement.",
        "warranty": "Assurance or guarantee about conditions, goods, or services.",
        "severability": "If one part is invalid, the rest of the contract stays effective."
    }
