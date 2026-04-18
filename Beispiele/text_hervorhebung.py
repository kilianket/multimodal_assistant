def highlight_verbs(text):
    doc = nlp(text)

    highlighted = []

    for token in doc:
        if token.pos_ == "VERB":
            highlighted.append(f"<mark>{token.text}</mark>")
        else:
            highlighted.append(token.text)

    return " ".join(highlighted)