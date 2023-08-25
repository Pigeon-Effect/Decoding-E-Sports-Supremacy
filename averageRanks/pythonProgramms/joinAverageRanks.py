import os
import csv

def merge_csv_files(input_folder, output_file):
    csv_files = [f for f in os.listdir(input_folder) if f.endswith('.csv')]

    if not csv_files:
        print("No CSV files found in the input folder.")
        return

    country_data = {}  # Ein Dictionary, um Daten nach Ländernamen zu gruppieren
    all_columns = set()  # Alle einzigartigen Spaltennamen über alle CSV-Dateien

    for csv_file in csv_files:
        with open(os.path.join(input_folder, csv_file), 'r') as infile:
            reader = csv.reader(infile)
            header = next(reader)  # Header-Zeile

            all_columns.update(header[1:])  # Füge Spaltennamen zur Menge hinzu

            for row in reader:
                country = row[0]
                country_data.setdefault(country, {}).update({header[i]: row[i] for i in range(1, len(row))})

    # Ermittle das Maximum für jede Spalte
    column_max = {}
    for col in all_columns:
        column_max[col] = max(float(country_data[country].get(col, 0)) for country in country_data)

    # Sortiere Länder alphabetisch und erstelle eine Liste für die CSV-Ausgabe
    sorted_countries = sorted(country_data.keys())
    output_rows = []

    for country in sorted_countries:
        country_row = [country]
        for col in all_columns:
            value = country_data[country].get(col)
            if value is None:
                value = column_max[col] + 1
            country_row.append(value)
        output_rows.append(country_row)

    # Schreibe die Daten in die Ausgabedatei
    with open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['Country'] + sorted(all_columns))  # Header-Zeile schreiben
        writer.writerows(output_rows)

# Beispielaufruf
input_folder = 'averageRanks'  # Ordner mit den CSV-Dateien
output_file = 'merged_data.csv'  # Ausgabedatei für die zusammengesetzten Daten

merge_csv_files(input_folder, output_file)
