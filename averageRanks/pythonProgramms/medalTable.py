import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Lese die Bump Chart-Daten aus der CSV-Datei ein
input_file = 'cleanedBumpChart.csv'  # Passe den Dateinamen an
bump_chart_data = pd.read_csv(input_file)

fluor_colors = ['#567CFF', '#8EA8FF', '#7A78FF', '#D875FF', '#8D4BE0', '#CCFF00', '#7FFF00', '#39FF14',
                '#1F51FF', '#0A4E43', '#029782', '#ABC65F', '#83018E', '#0D8596', '#B624C1', '#EF40FF',
                '#9457E4', '#1562C1', '#350B99', '#E923F4', '#72076E', '#12E195', '#0FF985', '#FDE802',
                '#FF901B', '#FC5E01', '#79FDF9', '#03EDF4', '#03CDFF', '#2368FB', '#5A32FC', '#D1FE49',
                '#FF1F4F', '#BE0357', '#017562', '#F5F232', '#5600F4']

fig = px.line(
    bump_chart_data,
    x='Game Genre',
    y='Ranking',
    color='Country',
    labels={'Ranking': 'Rank'},
    markers=True,
    line_shape='spline',
)

# Passe das Layout an
fig.update_layout(
    xaxis_title='Game Genre',
    yaxis_title='Rank',
    font=dict(color='white'),  # Schriftfarbe anpassen
    plot_bgcolor='black',  # Hintergrundfarbe des Plots
    legend=dict(title='Country'),  # Legenden-Titel
    showlegend=False,  # Legende anzeigen
    paper_bgcolor='black',
    yaxis=dict(
        range=[39,50],
    ),
)

#fig.update_traces(
#    mode='lines+markers',
#    marker=dict(size=25, symbol='circle', color=fluor_colors),  # Verwende Rechtecke als Symbole
#    line=dict(width=2,color=fluor_colors),
#)

for i, country in enumerate(bump_chart_data['Country'].unique()):
    color = fluor_colors[i % len(fluor_colors)]  # Wähle eine Farbe aus der Liste
    country_data = bump_chart_data[bump_chart_data['Country'] == country]

    fig.add_trace(go.Scatter(
        x='Game Genre',
        y='Ranking',
        line_shape='spline',
        line=dict(width=2, color=color),  # Setze die Linienstärke und Farbe
        marker=dict(size=8, symbol='circle', color=color),  # Setze die Markersymbole und Farbe
        name=country
    ).data[0])

# Zeige den Bump Chart an
fig.show()
