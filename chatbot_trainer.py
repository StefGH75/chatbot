"""
Autorin: Stefanie Millow
Chatbot Trainer für die Chatbot Gui (chatbot_gui.py)
Das Training erfolgt mit Hilfe der Datei: ChatbotTraining.csv

"""
# Pakete importieren
import string
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder #Zum Umwandeln von Text-Labels in Zahlen
#from sklearn.feature_extraction.text import CountVectorizer
import nltk #Für Sprachverarbeitung
from nltk.stem.porter import PorterStemmer #Zum Reduzieren von Wörtern auf ihren Wortstamm

#nltk.download("punkt_tab")

def trainiere_chatbot():
    """Funktion zum Trainieren des Chatbots"""

    #CSV-Datei laden:
    df = pd.read_csv("ChatbotTraining.csv")

    #Nur "patterns" als Eingabe, "tag" als Ziel:
    X = df["patterns"] #Satz
    y = df["tag"] #Art des Satzes

    #Ziel-Labels in Zahlen umwandeln:
    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(y)

    #Vorverarbeitung: Tokenisieren & Stemming:
    stemmer = PorterStemmer()

    def preprocess(text):
        """Funktion zur Vorverarbeitung von Text: Tokenisieren + Stemmings"""
        #Text in Wörter aufteilen:
        tokens = nltk.word_tokenize(text)
        #Satzzeichen entfernen:
        tokens = [word for word in tokens if word not in string.punctuation]
        #alles in Kleinbuchstaben & auf Wortstamm reduzieren:
        stemmed = [stemmer.stem(word.lower()) for word in tokens]
        return stemmed #Rückgabe als Liste

    X_processed = X.apply(preprocess)

    #Vokabular erstellen (alle einzigartigen Wörter):
    vocab = sorted(set(word for tokens in X_processed for word in tokens))
    #set macht daraus Liste einzigartigerWörter, die durch sorted alphabetisch
    #sortiert werden (nicht zwingend notwendig)

    #Manuelle Feature-Erstellung (1 wenn Wort vorkommt, sonst 0):
    def text_to_features(tokens):
        return [1 if word in tokens else 0 for word in vocab]

    #Feature-Matrix erstellen:
    X_features = X_processed.apply(text_to_features).tolist()
    #apply: jeder Eintrag einzeln aufgerufen, jede Liste
    #von Tokens in Vektor aus 0 und 1 verwandelt & dann in Liste umgewandelt

    #Decision-Tree trainieren:
    model = DecisionTreeClassifier()
    model.fit(X_features, y)

    # Antwort-Suche: Lade responses-Spalte
    tag_to_response = df.groupby("tag")["responses"].apply(list).to_dict()
    #Groupierung nach tag, pro Gruppe interessiere ich mich für die Spalte
    # responses. Diese Werte werden dann in Liste umgewandelt, das wird dann
    # in dic umgewandelt mit tag als Schlüssel

    return {
            "model": model,
            "preprocess": preprocess,
            "text_to_features": text_to_features,
            "vocab": vocab,
            "label_encoder": label_encoder,
            "tag_to_response": tag_to_response
        }

#Nur ausführen, wenn direkt gestartet:
if __name__ == "__main__":
    components = trainiere_chatbot()
    print("Das Chatbot-Modell wurde trainiert und ist einsatzbereit.")
