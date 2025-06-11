import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import numpy as np

# 1. CSV-Datei einlesen
df = pd.read_csv("ChatbotTraining.csv")

# 2. Textdaten vorbereiten
X = df["patterns"].copy()  # Input-Sätze
y = df["tag"].copy()       # Zielkategorie (z. B. greeting, goodbye)

# 3. Zielwerte numerisch kodieren
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)  # z. B. ["greeting", "goodbye"] → [0, 1]

# 4. Bag of Words auf patterns anwenden (mit Wortfrequenz)
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(X)  # → sparse Matrix mit Häufigkeiten (nur 1 gespeichert)

# 5. Train/Test-Split mit stratify
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# 6. Decision Tree Modell trainieren
decicision_tree = DecisionTreeClassifier()
decicision_tree.fit(X_train, y_train)

# 7. Vorhersage & Auswertung
y_pred = decicision_tree.predict(X_test)
print(f"Genauigkeit: {accuracy_score(y_test, y_pred):.2f}")

