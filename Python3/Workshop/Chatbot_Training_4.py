# Pakete importieren
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder #Zum Umwandeln von Text-Labels in Zahlen
from sklearn.feature_extraction.text import CountVectorizer
import nltk #Für Sprachverarbeitung
from nltk.stem.porter import PorterStemmer #Zum Reduzieren von Wörtern auf ihren Wortstamm

nltk.download("punkt_tab")

# CSV-Datei laden
df = pd.read_csv("ChatbotTraining.csv")

# Nur "patterns" als Eingabe, "tag" als Ziel
X = df["patterns"]
y = df["tag"]

# Ziel-Labels in Zahlen umwandeln
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# Vorverarbeitung: Tokenisieren & Stemming
stemmer = PorterStemmer()

# Funktion zur Vorverarbeitung von Text: Tokenisieren + Stemmings
def preprocess(text):
    tokens = nltk.word_tokenize(text) #Text in Wörter aufteilen
    stemmed = [stemmer.stem(word.lower()) for word in tokens] #Kleinbuchstaben & Wortstamm
    return stemmed #Rückgabe als Liste

X_processed = X.apply(preprocess)

#Vokabular erstellen (alle einzigartigen Wörter):
vocab = sorted(set(word for tokens in X_processed for word in tokens))

# Manuelle Feature-Erstellung (1 wenn Wort vorkommt, sonst 0)
def text_to_features(tokens):
    return [1 if word in tokens else 0 for word in vocab]

# Feature-Matrix erstellen
X_features = X_processed.apply(text_to_features).tolist()

# Bag of Words erstellen
#vectorizer = CountVectorizer()
#X_vectorized = vectorizer.fit_transform(X)

# Decision-Tree trainieren
model = DecisionTreeClassifier()
model.fit(X_features, y)

# Terminal-Eingabe + Vorhersage
while True:
    user_input = input("\nGib einen Satz ein (oder 'exit' zum Beenden): ")
    if user_input.lower() == "exit":
        break

    # Vorverarbeitung + Vektorisierung
    user_processed = preprocess(user_input)
    user_vector = [1 if word in user_processed else 0 for word in vocab]

    # Vorhersage
    prediction = model.predict([user_vector])
    predicted_class = label_encoder.inverse_transform(prediction)

    print("Vorhergesagte Klasse:", predicted_class[0])
