import re

def replace_comma_with_dot_and_save(input_file, output_file):
    # Einlesen der CSV-Datei als Zeichenkette
    with open(input_file, 'r') as file:
        csv_data = file.read()

    # Ersetzen aller Kommas durch Punkte
    csv_data_with_dots = re.sub(r',', '.', csv_data)

    # Schreiben der bearbeiteten Daten in eine neue CSV-Datei
    with open(output_file, 'w') as file:
        file.write(csv_data_with_dots)

# Beispielaufruf der Funktion
replace_comma_with_dot_and_save('MulitFactorTable#8.csv', 'MulitFactorTable#9.csv')
