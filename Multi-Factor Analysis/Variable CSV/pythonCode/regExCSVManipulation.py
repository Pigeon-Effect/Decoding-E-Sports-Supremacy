import re
import pandas as pd

def remove_star_and_spaces(text):
    # Entferne '*' und Leerzeichen, die direkt davor stehen
    cleaned_text = re.sub(r'\s+\*', '', text)
    return cleaned_text

# Lade die CSV-Datei in einen DataFrame
csv_filename = "CountriesByPPPGDPperCapita.csv"  # Ersetze "deine_datei.csv" durch den Dateinamen deiner CSV-Datei
df = pd.read_csv(csv_filename)

# Wende die Funktion auf die relevanten Spalten an
columns_to_clean = ["Country", "GDP (PPP per Capita)"]  # Ersetze "Spalte1", "Spalte2" usw. durch die Spaltennamen deiner CSV-Datei

for column in columns_to_clean:
    df[column] = df[column].apply(remove_star_and_spaces)

# Speichere den bereinigten DataFrame zurück in eine neue CSV-Datei
cleaned_csv_filename = "gdp_ppp_perCapita_manipulated.csv"  # Du kannst hier den gewünschten Namen für die neue Datei angeben
df.to_csv(cleaned_csv_filename, index=False)

print("Bereinigte CSV-Datei wurde erstellt: ", cleaned_csv_filename)
