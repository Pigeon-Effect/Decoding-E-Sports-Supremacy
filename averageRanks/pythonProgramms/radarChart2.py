import plotly.graph_objects as go
import pandas as pd
import plotly.io as pio

# Definiere die gewünschten Farben (transparent)
fluor_colors_lines = ['rgba(86, 124, 255, 0.6)', 'rgba(142, 168, 255, 0.6)', 'rgba(122, 120, 255, 0.6)',
                'rgba(216, 117, 255, 0.6)', 'rgba(141, 75, 224, 0.6)', 'rgba(204, 255, 0, 0.6)',
                'rgba(127, 255, 0, 0.6)', 'rgba(57, 255, 20, 0.6)', 'rgba(31, 81, 255, 0.6)',
                'rgba(10, 78, 67, 0.6)', 'rgba(2, 151, 130, 0.6)', 'rgba(171, 198, 95, 0.6)',
                'rgba(131, 1, 142, 0.6)', 'rgba(13, 133, 150, 0.6)', 'rgba(182, 36, 193, 0.6)',
                'rgba(239, 64, 255, 0.6)', 'rgba(148, 87, 228, 0.6)', 'rgba(21, 98, 193, 0.6)',
                'rgba(53, 11, 153, 0.6)', 'rgba(233, 35, 244, 0.6)', 'rgba(114, 7, 110, 0.6)',
                'rgba(18, 225, 149, 0.6)', 'rgba(15, 249, 133, 0.6)', 'rgba(253, 232, 2, 0.6)',
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
                'rgba(239, 64, 255, 0.2)', 'rgba(148, 87, 228, 0.2)', 'rgba(21, 98, 193, 0.2)',
                'rgba(53, 11, 153, 0.2)', 'rgba(233, 35, 244, 0.2)', 'rgba(114, 7, 110, 0.2)',
                'rgba(18, 225, 149, 0.2)', 'rgba(15, 249, 133, 0.2)', 'rgba(253, 232, 2, 0.2)',
                'rgba(255, 144, 27, 0.2)', 'rgba(252, 94, 1, 0.2)', 'rgba(121, 253, 249, 0.2)',
                'rgba(3, 237, 244, 0.2)', 'rgba(3, 205, 255, 0.2)', 'rgba(35, 104, 251, 0.2)',
                'rgba(90, 50, 252, 0.2)', 'rgba(209, 254, 73, 0.2)', 'rgba(255, 31, 79, 0.2)',
                'rgba(190, 3, 87, 0.2)', 'rgba(1, 117, 98, 0.2)', 'rgba(245, 242, 50, 0.2)',
                'rgba(86, 0, 244, 0.2)']

# Lese die CSV-Datei ein
input_csv = 'InvertedSelection#2AverageRanks.csv'  # Passe den Dateinamen an
df = pd.read_csv(input_csv)

# Extrahiere Ländernamen und Attributnamen
countries = df["Country"].tolist()
attributes = df.columns[1:].tolist()

fig = go.Figure()

# Füge Daten für jedes Land hinzu
for i, country in enumerate(countries):
    values = df.iloc[i, 1:].tolist()  # Verwende die Daten direkt aus dem DataFrame

    # Füge das erste Element am Ende hinzu, um den Kreis zu schließen
    values.append(values[0])
    attributes.append(attributes[0])

    trace = go.Scatterpolar(
        r=values,
        theta=attributes,
        fill='toself',
        fillcolor=fluor_colors_shapes[i % len(fluor_colors_shapes)],  # Verwende die gewünschten Farben
        line=dict(color=fluor_colors_lines[i % len(fluor_colors_lines)]),  # Transparente Farbe für Linien
        name=str(country),
        text=[country] * len(df['Country']),
        hovertemplate='<b>%{text}</b><br>Game Genre: %{theta}<br>Average Normalized Inverted Rank: %{r:.3f}',
        hoverlabel_namelength=0,

    )
    if str(country) in ['Italy', 'Philippines']:
        trace.visible = True
    else:
        trace.visible = 'legendonly'
    fig.add_trace(trace)

# Passe das Layout an
fig.update_layout(
    polar=dict(
        bgcolor='black',  # Hintergrundfarbe des Kreises auf schwarz ändern
        radialaxis=dict(
            visible=True,
            range=[0, 1],
            tickvals=[],  # Keine Tick-Markierungen
            showline=False,
        )),
    showlegend=True,
    paper_bgcolor='black',
    font=dict(color='white'),
    legend=dict(
        orientation="h",  # Legende vertikal anzeigen
        x=1.15,  # Legende rechts vom Graphen positionieren
        y=0.75,  # Obere Ecke der Legende
        bgcolor='rgba(0,0,0,0)',  # Transparente Hintergrundfarbe
        bordercolor='rgba(0,0,0,0)'  # Transparenter Rahmen
    ))


# Zeige das Radar Chart an
pio.write_html(fig, 'radarChart#1.html')
fig.show()
