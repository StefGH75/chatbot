# Pakete importieren
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer

# CSV-Datei laden
df = pd.read_csv("ChatbotTraining.csv")

# Nur die relevanten Spalten nehmen
X = df["patterns"]
y = df["tag"]

# Labels codieren
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# Bag of Words ohne Stemming oder nltk
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Modell trainieren
model = DecisionTreeClassifier()
model.fit(X_vectorized, y)

# Terminaleingabe + Vorhersage
while True:
    user_input = input("\nGib einen Satz ein (oder 'exit' zum Beenden): ")
    if user_input.lower() == "exit":
        break

    user_vector = vectorizer.transform([user_input])
    prediction = model.predict(user_vector)
    predicted_class = label_encoder.inverse_transform(prediction)

    print("Vorhergesagte Klasse:", predicted_class[0])
