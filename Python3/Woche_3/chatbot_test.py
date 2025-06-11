#Pakete der Bibliotheken importieren:
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

#CSV-Datei importieren:
df = pd.read_csv("ChatbotTraining.csv")

#Daten-Ausgabe:
print(df.head()) #Die ersten 5 Zeilen der Daten anzeigen lassen
print(df.describe()) #Statistiken der Daten anzeigen lassen (Anzahl, Durchschnitt, min, max, percentile etc.)

label_encoder = LabelEncoder() #Aus Text (greeting, joke) Zahlen generieren(0,1)
df["tag"] = label_encoder.fit_transform(df["tag"]) #kodiert Textwerte zu Zahlen und überschreibt originalspalte in df
print(df.head())
print(df.describe())

#Features und Label trennen:
X = df.drop(columns=["tag"])
#doppelte eckige Klammern, da mehrere Spalten, X groß: Konvention im ML
y = df["tag"] #Label = Zielwert

#Daten in Training und Test aufteilen:
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
#80% gehen in X_train, y_train, 20% in X_test, y_test
# random_state=42, zufällige Aufteilung (mit beliebiger Zahl),die immer gleich bleibt, stratify=y bedeutet 
#Aufteilung repräsentativ in Bezug auf Verteilung der Zielvariable y ist (weil unbalancierte Anteile Klassen)
#so bleibt relativer Anteil der Klassen in Trainings und Testset gleich

print(f"X_train: {len(X_train)}")
print(X_train.shape)
len(X_test)
len(y_train)
len(y_test)

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