import spacy

nlp = spacy.load("de_core_news_sm")

def analyze(text):
    doc = nlp(text)

    tokens = [{"text": t.text, "pos": t.pos_} for t in doc]
    verbs = [t.text for t in doc if t.pos_ == "VERB"]
    nouns = [t.text for t in doc if t.pos_ == "NOUN"]

    return {
        "tokens": tokens,
        "verbs": verbs,
        "nouns": nouns
    }

def highlight_verbs(text):
    doc = nlp(text)
    out = []

    for t in doc:
        if t.pos_ == "VERB":
            out.append(f"<mark>{t.text}</mark>")
        else:
            out.append(t.text)

    return " ".join(out)