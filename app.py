import streamlit as st
from speech_to_text import transcribe_audio
from nlp_analysis import analyze, highlight_verbs
from image_generator import get_image_from_nouns

st.set_page_config(page_title="Multimodaler Sprach-Assistent")

st.title("🎤 Multimodaler Sprach-Assistent")

st.write("Lade eine Audio-Datei hoch (wav/mp3) oder gib Text ein.")

mode = st.radio("Modus", ["Text", "Audio"])

text = ""

if mode == "Text":
    text = st.text_input("Text eingeben")
else:
    audio = st.file_uploader("Audio hochladen", type=["wav", "mp3", "m4a"])
    if audio:
        text = transcribe_audio(audio)

if text:
    st.subheader("🧾 Original Text")
    st.write(text)

    analysis = analyze(text)

    st.subheader("🧠 Analyse")
    st.json(analysis)

    st.subheader("🟡 Verben markiert")
    st.markdown(highlight_verbs(text), unsafe_allow_html=True)

    if analysis["nouns"]:
        st.subheader("🖼 Bild aus Nomen")
        query = " ".join(analysis["nouns"][:3])
        img_url = get_image_from_nouns(query)
        st.image(img_url)