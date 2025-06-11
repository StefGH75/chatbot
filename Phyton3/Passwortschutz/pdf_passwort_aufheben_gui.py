import pikepdf
import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

def entschluessle_pdf(eingabe_pfad, ausgabe_pfad, passwort):
    """
    Entschlüsselt eine PDF-Datei mit dem angegebenen Passwort.
    Nutzung der pikepdf Bibliothek für die Entschlüsselung.
    Die Bibliothek wird mit pip installiert.
        
    """
    try:
        # Überprüft ob Eingabedatei existiert
        if not os.path.exists(eingabe_pfad):
            messagebox.showerror("Fehler", f"Eingabedatei nicht gefunden: {eingabe_pfad}")
            return False

        try:
            # Versucht die PDF mit dem Passwort zu öffnen
            pdf = pikepdf.open(eingabe_pfad, password=passwort)
            
            # Stellt sicher, dass das Ausgabeverzeichnis existiert
            ausgabe_verzeichnis = os.path.dirname(ausgabe_pfad)
            if ausgabe_verzeichnis and not os.path.exists(ausgabe_verzeichnis):
                os.makedirs(ausgabe_verzeichnis)
            
            # Speichert die entschlüsselte PDF
            pdf.save(ausgabe_pfad)
            
            # Schließt die PDF-Datei um Ressourcen freizugeben
            pdf.close()
            messagebox.showinfo("Erfolg", "PDF erfolgreich entschlüsselt und gespeichert.")
            return True
            
        except pikepdf.PasswordError:
            messagebox.showerror("Fehler", "Passwort ist nicht korrekt.")
            return False
        except Exception as e:
            messagebox.showerror("Fehler", f"Fehler beim Entschlüsseln: {str(e)}")
            return False

    except Exception as e:
        messagebox.showerror("Fehler", f"Fehler beim Entschlüsseln: {str(e)}")
        return False

class PDFEntschlusselerGUI:
    """
    GUI für den PDF-Entschlüsseler
    Bietet eine benutzerfreundliche Oberfläche zum Entschlüsseln von PDF-Dateien.
    """
    def __init__(self, root):
        """
        Initialisiert die GUI.
        """
        self.root = root
        self.root.title("PDF Entschlüsseler")
        self.root.resizable(False, False)  # Verhindert Größenänderung des Fensters
        
        # Hauptframe mit Padding für besseren Abstand zum Fensterrand
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Eingabe-PDF: Label, Eingabefeld und Durchsuchen-Button
        ttk.Label(main_frame, text="Vollständiger Pfad zur verschlüsselten PDF-Datei\n(inkl. Dateiname):").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.eingabe_pfad = tk.StringVar()  # Variable für den Eingabepfad
        ttk.Entry(main_frame, textvariable=self.eingabe_pfad, width=60).grid(row=0, column=1, padx=5)
        ttk.Button(main_frame, text="Durchsuchen", command=self.eingabe_durchsuchen).grid(row=0, column=2)
        
        # Ausgabe-PDF: Label, Eingabefeld und Durchsuchen-Button
        ttk.Label(main_frame, text="Vollständiger Pfad für die entschlüsselte PDF-Datei\n(inkl. Dateiname):").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.ausgabe_pfad = tk.StringVar()  # Variable für den Ausgabepfad
        ttk.Entry(main_frame, textvariable=self.ausgabe_pfad, width=60).grid(row=1, column=1, padx=5)
        ttk.Button(main_frame, text="Durchsuchen", command=self.ausgabe_durchsuchen).grid(row=1, column=2)
        
        # Passwort: Label und Eingabefeld (maskiert mit *)
        ttk.Label(main_frame, text="Passwort für die PDF-Datei:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.passwort = tk.StringVar()  # Variable für das Passwort
        ttk.Entry(main_frame, textvariable=self.passwort, show="*", width=60).grid(row=2, column=1, padx=5)
        
        # Entschlüsseln-Button in der Mitte
        ttk.Button(main_frame, text="PDF Entschlüsseln", command=self.entschluesseln).grid(row=3, column=1, pady=20)
        
        # Status-Anzeige für Feedback an den Benutzer
        self.status_var = tk.StringVar()
        ttk.Label(main_frame, textvariable=self.status_var).grid(row=4, column=0, columnspan=3, pady=5)
        
    def eingabe_durchsuchen(self):
        """
        Öffnet einen Dateiauswahl-Dialog für die verschlüsselte PDF-Datei.
        Setzt automatisch einen Vorschlag für den Ausgabepfad, wenn Durchsuchen genutzt wird.
        """
        datei = filedialog.askopenfilename(
            title="Verschlüsselte PDF auswählen",
            filetypes=[("PDF Dateien", "*.pdf"), ("Alle Dateien", "*.*")]
        )
        if datei:
            # Fügt .pdf hinzu, wenn keine Dateiendung vorhanden ist
            if not datei.lower().endswith('.pdf'):
                datei += '.pdf'
            self.eingabe_pfad.set(datei)
            # Automatisch Ausgabepfad vorschlagen
            verzeichnis = os.path.dirname(datei)
            dateiname = os.path.basename(datei)
            neuer_name = f"entschluesselt_{dateiname}"
            self.ausgabe_pfad.set(os.path.join(verzeichnis, neuer_name))
    
    def ausgabe_durchsuchen(self):
        """
        Öffnet einen Dateiauswahl-Dialog für den Speicherort der entschlüsselten PDF-Datei.
        """
        datei = filedialog.asksaveasfilename(
            title="Speicherort für entschlüsselte PDF",
            defaultextension=".pdf",
            filetypes=[("PDF Dateien", "*.pdf"), ("Alle Dateien", "*.*")]
        )
        if datei:
            # Fügt .pdf hinzu, wenn keine Dateiendung vorhanden ist
            if not datei.lower().endswith('.pdf'):
                datei += '.pdf'
            self.ausgabe_pfad.set(datei)
    
    def entschluesseln(self):
        """
        Startet den Entschlüsselungsprozess.
        Überprüft die Eingaben und ruft die Entschlüsselungsfunktion auf.
        """
        eingabe = self.eingabe_pfad.get()
        ausgabe = self.ausgabe_pfad.get()
        passwort = self.passwort.get()
        
        # Fügt .pdf hinzu, wenn keine Dateiendung vorhanden ist
        if eingabe and not eingabe.lower().endswith('.pdf'):
            eingabe += '.pdf'
            self.eingabe_pfad.set(eingabe)
        if ausgabe and not ausgabe.lower().endswith('.pdf'):
            ausgabe += '.pdf'
            self.ausgabe_pfad.set(ausgabe)
        
        # Überprüft ob alle Felder ausgefüllt sind
        if not eingabe or not ausgabe or not passwort:
            messagebox.showwarning("Warnung", "Bitte füllen Sie alle Felder aus.")
            return
        
        # Aktualisiert Status und startetEntschlüsselung
        self.status_var.set("Entschlüssele PDF...")
        self.root.update()
        
        if entschluessle_pdf(eingabe, ausgabe, passwort):
            self.status_var.set("PDF erfolgreich entschlüsselt und gespeichert!")
        else:
            self.status_var.set("Fehler beim Entschlüsseln der PDF.")

# === Hauptprogramm ===
if __name__ == "__main__":
    root = tk.Tk()
    app = PDFEntschlusselerGUI(root)
    root.mainloop()
