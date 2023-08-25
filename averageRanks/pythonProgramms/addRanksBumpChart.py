import pandas as pd

def expand_and_invert_csv(input_file, output_file):
    # Lese die CSV-Datei ein
    df = pd.read_csv(input_file)

    # Erstelle ein Set aller Länder, die in der CSV vorkommen
    all_countries = set(df['Country'])

    # Erweitere die CSV für fehlende Länder in jedem Genre
    expanded_data = []
    genres = df['Game Genre'].unique()
    for genre in genres:
        genre_data = df[df['Game Genre'] == genre]
        existing_countries = set(genre_data['Country'])

        # Füge fehlende Länder mit Rang 50 hinzu
        missing_countries = all_countries - existing_countries
        for country in missing_countries:
            expanded_data.append({'Game Genre': genre, 'Country': country, 'Ranking': 50})

        # Füge die vorhandenen Daten hinzu
        expanded_data.extend(genre_data.to_dict('records'))

    # Erstelle ein DataFrame aus den erweiterten Daten
    expanded_df = pd.DataFrame(expanded_data)

    # Invertiere die Rang-Werte
    expanded_df['Ranking'] = 50 - expanded_df['Ranking']

    # Speichere das erweiterte und invertierte DataFrame als CSV-Datei
    expanded_df.to_csv(output_file, index=False)

# Beispielaufruf
input_file = 'bump_chart_data.csv'  # Passe den Dateinamen an
output_file = 'cleanedBumpChart.csv'  # Passe den gewünschten Ausgabedateinamen an

expand_and_invert_csv(input_file, output_file)
