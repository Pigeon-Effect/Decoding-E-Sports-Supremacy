import pandas as pd

def invert_and_normalize_rankings(input_file, output_file):
    # Lese die CSV-Datei ein
    df = pd.read_csv(input_file)

    # Ignoriere die erste Spalte (Ländernamen) und die erste Zeile (Bezeichnungen)
    data = df.iloc[:, 1:]

    # Invertiere die Ranking-Werte
    max_values = data.max()
    inverted_data = max_values - data

    # Normalisiere die invertierten Werte auf den Bereich [0, 1]
    normalized_data = (inverted_data - inverted_data.min()) / (inverted_data.max() - inverted_data.min())

    # Speichere die normalisierten Daten in der Ausgabedatei
    normalized_df = pd.concat([df.iloc[:, 0], normalized_data], axis=1)
    normalized_df.to_csv(output_file, index=False)

# Beispielaufruf
input_file = 'AllAverageRanks.csv'  # Eingabedatei mit den Ranking-Daten
output_file = 'NormalizedInvertedAllAverageRanks.csv'  # Ausgabedatei für die normalisierten, invertierten Daten

invert_and_normalize_rankings(input_file, output_file)
