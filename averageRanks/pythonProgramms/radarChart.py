import plotly.graph_objects as go
import pandas as pd

'''
# Definiere die gewünschten Farben
fluor_colors = ['#567CFF', '#8EA8FF', '#7A78FF', '#D875FF', '#8D4BE0', '#CCFF00', '#7FFF00', '#39FF14',
                '#1F51FF', '#0A4E43', '#029782', '#ABC65F', '#83018E', '#0D8596', '#B624C1', '#EF40FF',
                '#9457E4', '#1562C1', '#350B99', '#E923F4', '#72076E', '#12E195', '#0FF985', '#FDE802',
                '#FF901B', '#FC5E01', '#79FDF9', '#03EDF4', '#03CDFF', '#2368FB', '#5A32FC', '#D1FE49',
                '#FF1F4F', '#BE0357', '#017562', '#F5F232', '#5600F4']
'''

fluor_colors_lines = ['rgba(86, 124, 255, 0.6)', 'rgba(142, 168, 255, 0.6)', 'rgba(122, 120, 255, 0.6)',
                'rgba(216, 117, 255, 0.6)', 'rgba(141, 75, 224, 0.6)', 'rgba(204, 255, 0, 0.6)',
                'rgba(127, 255, 0, 0.6)', 'rgba(57, 255, 20, 0.6)', 'rgba(31, 81, 255, 0.6)',
                'rgba(10, 78, 67, 0.6)', 'rgba(2, 151, 130, 0.6)', 'rgba(171, 198, 95, 0.6)',
                'rgba(131, 1, 142, 0.6)', 'rgba(13, 133, 150, 0.6)', 'rgba(182, 36, 193, 0.6)',
                'rgba(239, 64, 255, 0.6)', 'rgba(148, 87, 228, 0.6)', 'rgba(21, 98, 193, 0.6)',
                'rgba(53, 11, 153, 0.6)', 'rgba(233, 35, 244, 0.6)', 'rgba(114, 7, 110, 0.6)',
                'rgba(18, 225, 149, 0.6', 'rgba(15, 249, 133, 0.6)', 'rgba(253, 232, 2, 0.6)',
                'rgba(255, 144, 27, 0.6)', 'rgba(252, 94, 1, 0.6)', 'rgba(121, 253, 249, 0.6)',
                'rgba(3, 237, 244, 0.6)', 'rgba(3, 205, 255, 0.6)', 'rgba(35, 104, 251, 0.6)',
                'rgba(90, 50, 252, 0.6)', 'rgba(209, 254, 73, 0.6)', 'rgba(255, 31, 79, 0.6)',
                'rgba(190, 3, 87, 0.6)', 'rgba(1, 117, 98, 0.6)', 'rgba(245, 242, 50, 0.6)',
                'rgba(86, 0, 244, 0.6)']

fluor_colors_shapes = ['rgba(86, 124, 255, 0.2)', 'rgba(142, 168, 255, 0.2)', 'rgba(122, 120, 255, 0.2)',
                'rgba(216, 117, 255, 0.2)', 'rgba(141, 75, 224, 0.2)', 'rgba(204, 255, 0, 0.2)',
                'rgba(127, 255, 0, 0.2)', 'rgba(57, 255, 20, 0.2)', 'rgba(31, 81, 255, 0.2)',
                'rgba(10, 78, 67, 0.2)', 'rgba(2, 151, 130, 0.2)', 'rgba(171, 198, 95, 0.2)',
                'rgba(131, 1, 142, 0.2)', 'rgba(13, 133, 150, 0.2)', 'rgba(182, 36, 193, 0.2)',
                'rgba(239, 64, 255, 0.6)', 'rgba(148, 87, 228, 0.6)', 'rgba(21, 98, 193, 0.6)',
                'rgba(53, 11, 153, 0.6)', 'rgba(233, 35, 244, 0.6)', 'rgba(114, 7, 110, 0.6)',
                'rgba(18, 225, 149, 0.6', 'rgba(15, 249, 133, 0.6)', 'rgba(253, 232, 2, 0.6)',
                'rgba(255, 144, 27, 0.6)', 'rgba(252, 94, 1, 0.6)', 'rgba(121, 253, 249, 0.6)',
                'rgba(3, 237, 244, 0.6)', 'rgba(3, 205, 255, 0.6)', 'rgba(35, 104, 251, 0.6)',
                'rgba(90, 50, 252, 0.6)', 'rgba(209, 254, 73, 0.6)', 'rgba(255, 31, 79, 0.6)',
                'rgba(190, 3, 87, 0.6)', 'rgba(1, 117, 98, 0.6)', 'rgba(245, 242, 50, 0.6)',
                'rgba(86, 0, 244, 0.6)']

# Lese die CSV-Datei ein
input_csv = 'SelectionAverageRanks.csv'  # Passe den Dateinamen an
df = pd.read_csv(input_csv)


# Extrahiere Ländernamen und Attributnamen
countries = df["Country"].tolist()
attributes = df.columns[1:].tolist()

fig = go.Figure()

# Füge Daten für jedes Land zum Radar Chart hinzu
for i, country in enumerate(countries):
    country_data = df[df["Country"] == country]
    values = country_data.iloc[0, 1:].tolist()  # Ignoriere den Ländernamen in der ersten Spalte

    # Füge das erste Element am Ende hinzu, um den Kreis zu schließen
    values.append(values[0])
    attributes.append(attributes[0])

    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=attributes,
        fill='toself',
        fillcolor=fluor_colors_shapes[i % len(fluor_colors_shapes)],  # Verwende die gewünschten Farben
        line=dict(color=fluor_colors_lines[i % len(fluor_colors_lines)]),  # Transparente Farbe für Linien
        name=country
    ))

# Passe das Layout an
fig.update_layout(
    polar=dict(
        bgcolor='white',
        radialaxis=dict(
            visible=True,
            range=[df.iloc[:, 1:].max().max() + 1, 0],  # Umgekehrte Skala
            showline=False,
            tickvals=[],  # Keine Tick-Markierungen
        )),
    showlegend=True,
    paper_bgcolor='black',
    font=dict(color='white'),
)

# Zeige das Radar Chart an
fig.show()
