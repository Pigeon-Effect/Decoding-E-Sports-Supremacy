import pandas as pd

def merge_countries(df, mapping_dict):
    # Führe die Länderbezeichnungen gemäß dem Mapping-Dict zusammen
    df['country'] = df['country'].replace(mapping_dict)

    # Gruppiere die Daten nach Land und berechne den Durchschnitt für die restlichen Spalten
    grouped_df = df.groupby('country', as_index=False).mean()

    return grouped_df

# Beispiel-Mapping-Dict für einige Länderbezeichnungen
mapping_dict = {
    'Russian Federation': 'Russia',
    'russian federation': 'Russia',
    'Iran, Islamic Republic of': 'Iran',
    'iran': 'Iran',
    'islamic republic of iran': 'Iran',
    'Syria': 'Syrian Arab Republic',
    'Syrian Arab Republic': 'Syrian Arab Republic',

}

# Beispielaufruf mit deiner vorhandenen DataFrame-Variable combined_df
combined_df = pd.concat(dataframes)
processed_df = merge_countries(combined_df, mapping_dict)

# Nun hast du ein DataFrame processed_df, in dem die Zeilen mit denselben Länderbezeichnungen zusammengeführt wurden.
