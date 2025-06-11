import re

def anonymize_input(text):
    # Namen (vereinfachte Annahme: zwei Wörter mit Großbuchstaben)
    text = re.sub(r'\b[A-ZÄÖÜ][a-zäöüß]+\s[A-ZÄÖÜ][a-zäöüß]+\b', '[NAME]', text)

    # E-Mail-Adressen
    text = re.sub(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', '[EMAIL]', text)

    # Telefonnummern
    text = re.sub(r'\b(\+?\d{1,3})?[\s.-]?(\(?\d{2,4}\)?)[\s.-]?\d{3,5}[\s.-]?\d{3,5}\b', '[TELEFON]', text)

    # Adressen (sehr grob – Straße mit Nummer)
    text = re.sub(r'\b([A-ZÄÖÜ][a-zäöüß]+(?:straße|weg|gasse|allee))\s\d+\b', '[ADRESSE]', text)

    # Geburtsdatum (z. B. 01.01.1990 oder 1990-01-01)
    text = re.sub(r'\b\d{1,2}[.\-/]\d{1,2}[.\-/]\d{2,4}\b', '[GEBURTSDATUM]', text)

    return text
