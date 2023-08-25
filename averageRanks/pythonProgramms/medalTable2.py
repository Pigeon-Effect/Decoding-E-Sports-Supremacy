import plotly.graph_objects as go
import pandas as pd
import plotly.io as pio

input_file = 'bump_chart_data.csv'  # Passe den Dateinamen an
bump_chart_data = pd.read_csv(input_file)


fluor_colors_lines = ['rgba(51, 51, 255, 0.3)', 'rgba(255, 0, 0, 0.3)', 'rgba(128, 255, 0, 0.3)',
                'rgba(255, 0, 255, 0.3)', 'rgba(255, 128, 0, 0.3)', 'rgba(51, 255, 255, 0.3)',
                'rgba(255, 255, 0, 0.3)', 'rgba(153, 51, 255, 0.3)', 'rgba(51, 255, 153, 0.3)',
                'rgba(10, 78, 67, 0.3)', 'rgba(2, 151, 130, 0.3)', 'rgba(171, 198, 95, 0.3)',
                'rgba(102, 0, 204, 0.3)', 'rgba(178, 255, 102, 0.3)', 'rgba(153, 153, 255, 0.3)',
]

fluor_colors_shapes = ['rgba(51, 51, 255, 1)', 'rgba(255, 0, 0, 1)', 'rgba(128, 255, 0, 1)',
                'rgba(255, 0, 255, 1)', 'rgba(255, 128, 0, 1)', 'rgba(51, 255, 255, 1)',
                'rgba(255, 255, 0, 1)', 'rgba(153, 51, 255, 1)', 'rgba(51, 255, 153, 1)',
                'rgba(10, 78, 67, 1)', 'rgba(2, 151, 130, 1)', 'rgba(171, 198, 95, 1)',
                'rgba(102, 0, 204, 1)', 'rgba(178, 255, 102, 1)', 'rgba(153, 153, 255, 1)',
]


fig = go.Figure()

for i, country in enumerate(bump_chart_data['Country'].unique()):
    lineColors = fluor_colors_lines[i % len(fluor_colors_lines)]  # Wähle eine Farbe aus der Liste
    shapeColors = fluor_colors_shapes[i % len(fluor_colors_shapes)]
    country_data = bump_chart_data[bump_chart_data['Country'] == country]

    trace = go.Scatter(
        x=country_data['Game Genre'],
        y=country_data['Ranking'],
        mode='lines+markers',
        line_shape='spline',
        line=dict(width=18, color=lineColors),  # Setze die Linienstärke und Farbe
        marker=dict(size=28, symbol='circle', color=shapeColors),  # Setze die Markersymbole und Farbe
        name=str(country),
        text=[country] * len(country_data['Country']),
        customdata=country_data['Ranking'],
        hovertemplate='<b>%{text}</b><br>Game Genre: %{x}<br>Rank: %{customdata}',
    )

    fig.add_trace(trace)

# Passe das Layout an
fig.update_layout(
    xaxis_title='Game Genre',
    yaxis_title='Rank',
    font=dict(color='white'),  # Schriftfarbe auf weiß setzen
    plot_bgcolor='black',  # Hintergrundfarbe des Plots auf schwarz setzen
    paper_bgcolor='black',
    legend=dict(title='Country', font=dict(color='white')),  # Legenden-Titel und Schriftfarbe auf weiß setzen
    title_font_color='white',  # Farbe des Titels auf weiß setzen
    showlegend=False,  # Legende ausblenden
    yaxis=dict(
        autorange='reversed',  # Umgedrehte Skala auf der y-Achse
    ),

)

fig.update_traces(hoverlabel_namelength=0)

# Zeige den Bump Chart an
pio.write_html(fig, 'medalTable#2.html')
fig.show()
