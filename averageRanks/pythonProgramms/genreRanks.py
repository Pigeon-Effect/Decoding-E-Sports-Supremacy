import csv

def filter_and_save_csv(input_file):
    with open(input_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # Speichere die Header-Zeile

        game_data = {}  # Ein Dictionary, um die Daten für jedes Spiel zu speichern

        for row in reader:
            game_name = row[0]
            if game_name not in game_data:
                game_data[game_name] = []  # Erstelle eine leere Liste für dieses Spiel
            game_data[game_name].append(row)  # Füge die Zeile zur Liste für das entsprechende Spiel hinzu

    # Für jedes Spiel speichere eine separate CSV-Datei
    for game_name, data_rows in game_data.items():
        output_file = f'{game_name}.csv'  # Dateiname basierend auf dem Spielnamen
        with open(output_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header)  # Schreibe die Header-Zeile in die Ausgabedatei
            writer.writerows(data_rows)  # Schreibe die Zeilen für dieses Spiel in die Ausgabedatei

# Beispielaufruf
input_file = 'cleanMOBA.csv'  # Eingabedatei mit 5 Spalten

filter_and_save_csv(input_file)
