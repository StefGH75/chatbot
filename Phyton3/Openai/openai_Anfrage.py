from anonymize_input import anonymize_input

from dotenv import load_dotenv
load_dotenv()

import requests
import os
import hashlib
import json

# Lade API-Schlüssel (z. B. aus Umgebungsvariable)
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("Bitte setze deine Umgebungsvariable 'OPENAI_API_KEY'.")

# OpenAI API-Endpunkt
url = "https://api.openai.com/v1/chat/completions"

# Nutzereingabe (interaktiv)
raw_prompt = input("Was möchtest du das KI-Modell fragen?\n> ").strip()
if not raw_prompt:
    print("Eingabe darf nicht leer sein.")
    exit()

user_prompt = anonymize_input(raw_prompt)


# Cache-Verzeichnis
CACHE_DIR = "cache"
os.makedirs(CACHE_DIR, exist_ok=True)

# Hash-Funktion für Dateinamen
def get_cache_filename(prompt):
    hashed = hashlib.sha256(prompt.encode("utf-8")).hexdigest()
    return os.path.join(CACHE_DIR, f"{hashed}.json")

# Versuch: Antwort aus Cache laden
cache_file = get_cache_filename(user_prompt)
if os.path.exists(cache_file):
    with open(cache_file, "r", encoding="utf-8") as f:
        response_data = json.load(f)
    print("\n Antwort aus Cache:\n")
else:
    # Anfrage an OpenAI vorbereiten
    payload = {
        "model": "gpt-4",  # Alternativ: "gpt-3.5-turbo"
        "messages": [
            {"role": "system", "content": "You are a helpful and concise assistant."},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 200
    }

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        response_data = response.json()
        with open(cache_file, "w", encoding="utf-8") as f:
            json.dump(response_data, f, ensure_ascii=False, indent=2)
        print("\n Antwort von OpenAI (neu generiert):\n")
    else:
        print(f" Fehler: {response.status_code}")
        print(response.text)
        exit()

# Antwortinhalt anzeigen
answer = response_data["choices"][0]["message"]["content"]
print(answer)


