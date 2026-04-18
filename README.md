# 🎙️ Multimodaler Sprach-Assistent

Ein intelligenter, Python-basierter multimodaler KI-Assistent, der gesprochene Sprache verarbeitet, linguistisch analysiert und visuell aufbereitet.

---

## 🚀 Projektübersicht

Der **Multimodale Sprach-Assistent** ist eine interaktive KI-Anwendung, die Sprache nicht nur in Text umwandelt, sondern diesen anschließend semantisch analysiert und visuell interpretiert.

Das System bildet eine vollständige KI-Pipeline:

> **Sprache → Text → Linguistische Analyse → Informationsextraktion → Visuelle Ausgabe**

---

## 🧠 Kernfunktionen

### 🎤 Spracherkennung (Speech-to-Text)
- Aufnahme von Sprache über ein Mikrofon
- Echtzeit-Umwandlung in Text
- Grundlage für alle weiteren Verarbeitungsschritte

---

### 🧾 Linguistische Analyse (NLP)

Nach der Transkription wird der Text sprachlich analysiert:

- Tokenisierung (Zerlegung in Wörter)
- Part-of-Speech Tagging (Wortarten-Erkennung)
- Identifikation zentraler Elemente:
  - Verben (Handlungen)
  - Nomen (Entitäten / Objekte)

---

### ✨ Visuelle Textverarbeitung
- Verben werden im Text farblich hervorgehoben
- Verbesserung der semantischen Lesbarkeit
- Strukturierte Darstellung von Handlungen

---

### 🖼️ Informationsextraktion & Visualisierung
- Extraktion relevanter Nomen (Objekte, Lebewesen, Orte)
- Zuordnung zu:
  - Bilddatenbanken **oder**
  - generativen KI-Modellen
- Automatische visuelle Darstellung im Chat

---

## 🎯 Ziel des Projekts

Das Projekt verfolgt die Kombination moderner KI-Technologien in einem System:

- 🎙️ Spracherkennung
- 🧠 Natural Language Processing (NLP)
- 🧾 Textanalyse & Strukturierung
- 🖼️ Bildzuordnung / Bildgenerierung
- 💬 Interaktive Benutzeroberfläche

Ziel ist es, Sprache nicht nur zu verarbeiten, sondern **verständlich, analysierbar und visuell erfahrbar zu machen**.

---

## ⚙️ Technische Pipeline

Die Verarbeitung erfolgt in mehreren klar getrennten Stufen:

### 🎤 1. Spracheingabe (Mikrofon)
Erfassung des Audiosignals über Hardware.

---

### 🗣️ 2. Speech-to-Text
Umwandlung akustischer Signale in digitalen Text.

---

### 🧾 3. Textvorverarbeitung
- Tokenisierung: Zerlegung in Wörter
- Normalisierung: Bereinigung von Satzzeichen und Formatierung

---

### 🧠 4. Linguistische Analyse (NLP)
- Part-of-Speech Tagging
- Erkennung von Verben und Nomen
- Strukturelle Textanalyse

---

### ✨ 5. Informationsextraktion
- Filterung relevanter Schlüsselbegriffe
- Fokus auf semantische Kerninformationen

---

### 🖼️ 6. Visuelle Zuordnung
- Abgleich der Begriffe mit Bilddatenbanken
- Optional: KI-basierte Bildgenerierung

---

### 💬 7. Ausgabe im Chat-Interface
- Markierter und strukturierter Text
- Visuelle Darstellung passender Inhalte

---

## 🧪 Beispiel-Workflow

**Input (gesprochene Sprache):**  
> „Der Hund läuft durch den Park“

**Analyse:**
- Verb: *läuft*
- Nomen: *Hund*, *Park*

**Output:**
- Markierter Text mit Hervorhebung der Handlung
- Visualisierung: Hund + Park als Bildkonzept

---

## 🛠️ Technologien

- Python 3.x
- SpeechRecognition / Whisper
- spaCy oder NLTK
- OpenCV (optional)
- PIL / Matplotlib
- Bild-APIs oder generative Modelle (z. B. Stable Diffusion)

---

## 📌 Projektstatus

- ✔ Spracherkennung integriert
- ✔ NLP-Pipeline implementiert
- ✔ Textanalyse & Markierung umgesetzt
- ⏳ Bildgenerierung / externe Datenanbindung (erweiterbar)

---

## 💡 Erweiterungsmöglichkeiten

- Emotionserkennung in Sprache
- Mehrsprachige Unterstützung
- Kontextbasierte Bildgenerierung
- Web-Interface (Flask / FastAPI)
- Echtzeit-Streaming-Verarbeitung

---

## 👨‍💻 Autoren

Dieses Projekt entstand im Rahmen eines Projekts im Bereich **Künstliche Intelligenz und Sprachverarbeitung** und umfasst die Python-basierte Entwicklung eines multimodalen KI-Systems.

--- 

## Projektteam

- Ruba Shehadeh  
- Godfrey Uchechukwu Atulegwu  
- Kilian Ketelhohn  

---

## 📄 Lizenz

Dieses Projekt darf für Bildungs- und Forschungszwecke frei verwendet werden.
