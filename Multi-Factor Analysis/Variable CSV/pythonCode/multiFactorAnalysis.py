import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio

# Read the CSV file
input_file = 'MulitFactorTable#9.csv'
data = pd.read_csv(input_file, delimiter=';')

# Konvertiere nicht-numerische Zeichen in numerische Werte
data = data.apply(pd.to_numeric, errors='coerce')

# Verwende die "corr" Funktion von Pandas, um die Korrelation zu berechnen
correlation_results = data.corr()['Total E-Sports Earning'].round(5)

# Sortiere die Korrelationswerte aufsteigend und entferne die abhängige Variable 'Total E-Sports Earning'
sorted_correlations = correlation_results.drop(['Total E-Sports Earning', 'Country']).sort_values()


# Methode zur Ermittlung der Anzahl fehlender Werte für jeden Index
def count_missing_values(df):
    return df.isna().sum()
missing_value_counts = count_missing_values(data[sorted_correlations.index])

# Sortiere die Korrelationswerte aufsteigend
sorted_correlations = correlation_results.drop(['Total E-Sports Earning', 'Country']).sort_values()

# Füge Leerzeichen vor den Index-Bezeichnungen hinzu, um den Abstand zu vergrößern
sorted_correlations.index = [idx + '  ' for idx in sorted_correlations.index]

# Erstelle ein Balkendiagramm mit Plotly
fig = go.Figure(go.Bar(
    x=sorted_correlations,
    y=sorted_correlations.index,
    text=sorted_correlations,
    textposition='outside',
    marker=dict(
        color=sorted_correlations,  # Verwende die Korrelationswerte für die Farbgebung
        colorscale='Viridis',  # Wähle eine Farbpalette (hier 'Viridis')
        colorbar=dict(title='Correlation<br>Value'),

    ),
    orientation='h',  # Horizontal ausgerichtete Balken
    hovertemplate='<b>%{y}</b><br><b>Correlation Value:</b> %{x:.5f}<br>'
                  '<b>Missing Value Count:</b> %{customdata}<br>',
    customdata=missing_value_counts.values,
    ),
)

# Anpassung des Layouts
fig.update_layout(
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(color='white'),
    showlegend=False,
    xaxis=dict(
        range=[0, 1.0],  # Festlegen des Bereichs für die X-Achse von -1.0 bis 1.0
    ),
)

#fig.update_traces(hoverlabel_namelength=0)

# Zeige das Balkendiagramm an
pio.write_html(fig, 'multiFactorAnalysis#2.html')

pio.show(fig)
