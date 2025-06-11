import pikepdf
import os
import glob

def finde_pdf_datei(basis_verzeichnis, datei_muster):
    """Sucht nach PDF-Dateien im angegebenen Verzeichnis und Unterverzeichnissen"""
    suche_pfad = os.path.join(basis_verzeichnis, "**", datei_muster)
    gefundene_dateien = glob.glob(suche_pfad, recursive=True)
    return gefundene_dateien

def entschluessle_pdf(eingabe_pfad, ausgabe_pfad, passwort):
    try:
        # Überprüfe ob Eingabedatei existiert
        if not os.path.exists(eingabe_pfad):
            print(f"Eingabedatei nicht gefunden: {eingabe_pfad}")
            print(f"Aktuelles Verzeichnis: {os.getcwd()}")
            
            # Suche nach der Datei im OneDrive-Ordner
            onedrive_pfad = os.path.expanduser("~/OneDrive")
            print(f"Suche nach PDF-Dateien im OneDrive-Ordner: {onedrive_pfad}")
            gefundene_dateien = finde_pdf_datei(onedrive_pfad, "*BISON*.pdf")
            
            if gefundene_dateien:
                print("\nGefundene PDF-Dateien:")
                for datei in gefundene_dateien:
                    print(f"- {datei}")
                print("\nBitte wählen Sie die korrekte Datei aus und passen Sie den Pfad im Code an.")
            return False

        print(f"Versuche PDF zu öffnen: {eingabe_pfad}")
        
        try:
            # Versuche die PDF mit dem Passwort zu öffnen
            pdf = pikepdf.open(eingabe_pfad, password=passwort)
            print(f"Erfolgreich mit Passwort: {passwort}")
            
            # Stelle sicher, dass das Ausgabeverzeichnis existiert
            ausgabe_verzeichnis = os.path.dirname(ausgabe_pfad)
            if ausgabe_verzeichnis and not os.path.exists(ausgabe_verzeichnis):
                os.makedirs(ausgabe_verzeichnis)
            
            # Speichere die entschlüsselte PDF
            print(f"Speichere entschlüsselte PDF unter: {ausgabe_pfad}")
            pdf.save(ausgabe_pfad)
            print("PDF erfolgreich entschlüsselt und gespeichert.")
            return True
            
        except pikepdf.PasswordError:
            print(f"Passwort ist nicht korrekt.")
            return False
        except Exception as e:
            print(f"Fehler beim Entschlüsseln: {str(e)}")
            return False

    except Exception as e:
        print(f"Fehler beim Entschlüsseln: {str(e)}")
        print(f"Fehlertyp: {type(e).__name__}")
        return False

def hole_benutzereingaben():
    print("\n=== PDF Entschlüsselung ===")
    print("Bitte geben Sie die erforderlichen Informationen ein:")
    
    # Eingabe-Pfad
    while True:
        eingabe_pfad = input("\nPfad zur verschlüsselten PDF-Datei: ").strip()
        if os.path.exists(eingabe_pfad):
            break
        print("Datei nicht gefunden. Bitte geben Sie einen gültigen Pfad ein.")
    
    # Ausgabe-Pfad
    while True:
        ausgabe_pfad = input("\nPfad für die entschlüsselte PDF-Datei: ").strip()
        ausgabe_verzeichnis = os.path.dirname(ausgabe_pfad)
        if not ausgabe_verzeichnis or os.path.exists(ausgabe_verzeichnis):
            break
        print("Ausgabeverzeichnis existiert nicht. Bitte geben Sie einen gültigen Pfad ein.")
    
    # Passwort
    passwort = input("\nPasswort für die PDF-Datei: ").strip()
    
    return eingabe_pfad, ausgabe_pfad, passwort

# === Hauptprogramm ===
if __name__ == "__main__":
    eingabe_pfad, ausgabe_pfad, pdf_passwort = hole_benutzereingaben()
    
    if entschluessle_pdf(eingabe_pfad, ausgabe_pfad, pdf_passwort):
        print("\nProzess erfolgreich abgeschlossen")
    else:
        print("\nProzess fehlgeschlagen")
