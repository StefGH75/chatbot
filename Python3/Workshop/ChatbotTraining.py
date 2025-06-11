#Pakete der Bibliotheken importieren:
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
import nltk
from nltk.stem.porter import PorterStemmer


#CSV-Datei importieren:
df = pd.read_csv("ChatbotTraining.csv")

#Daten-Ausgabe:
print(df.head()) #Die ersten 5 Zeilen der Daten anzeigen lassen
print(df.describe()) #Statistiken der Daten anzeigen lassen (Anzahl, Durchschnitt, min, max, percentile etc.)

#Features und Label trennen:
X = df.drop(columns=["tag"]).copy() #Kopie erstellen um eventuelle Fehler zu vermeiden, X groß: Konvention im ML
y = df["tag"].copy() #Label = Zielwert

#Umwandlung der Daten in Zahlen
label_encoder = LabelEncoder() #Aus Text (greeting, joke) Zahlen generieren(0,1)
df["tag"] = label_encoder.fit_transform(df["tag"]) #kodiert Textwerte zu Zahlen und überschreibt originalspalte in df
for column in X.columns: #prüft jede einzelne Spalte (patterns, response)
     if X[column].dtype == 'object': #d.type = object Prüft, ob Spalte Text enthält (in pandas für text/string)
         X[column] = label_encoder.fit_transform(X[column])
#Frage: eher OnehotEncoder für Feature-Spalten, da keine Reihenfolge?

print(df.head())

# kürzere Methode für Bag of Words (mit Wortfrequenz)
# vectorizer = CountVectorizer()
# X = vectorizer.fit_transform(X)  # sparse Matrix mit Häufigkeiten (nur 1 gespeichert)

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word): #grammatische Endungen werden entfernt
    stemmer = PorterStemmer()
    return stemmer.stem(word.lower())

def bag_of_words(sentence,words):
    sentence = tokenize(sentence)
    bow = [0] * len(words)
    #bow = np.zeros(len(words)) #leerer Vektor erstellt. np.zeros erzeugt array, das nur aus 0en besteht
                               # Länge des Arrays entspricht der Anzahl der Wörter im Vokabular
    # for i in range(len(words)):
    #     if words[i] in sentence_words:
    #         bag[i] = 1
    for i, word in enumerate(sentence):
        bow[i] = words.count(words)
    return bow

#Daten in Training und Test aufteilen:
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
#80% gehen in X_train, y_train, 20% in X_test, y_test
# random_state=42, zufällige Aufteilung (mit beliebiger Zahl), die immer gleich bleibt
#stratify = um Verteilung von Klassen (tag) in y in gleicher Relation zu behandeln, weil unterschiedliche Anzahl

#Aufsetzen eines Decision-Tree-Modells:
from sklearn.tree import DecisionTreeClassifier
decision_tree = DecisionTreeClassifier()

#Modell trainieren:
decision_tree.fit(X_train, y_train) #fit = lernen lassen. Lerne aus den Daten wie man das Ziel vorhersagt

#Vorhersage der Testdaten:
y_pred = decision_tree.predict(X_test)

print("Vorhersagen: ", y_pred)

#Genauigkeit/ accuracy ausgeben:
print("Genauigkeit:", accuracy_score(y_test, y_pred))

