import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
import plotly.offline as offline

# Load the CSV files and concatenate them into a single DataFrame
dataframes = []
years = range(1998, 2023)
for year in years:
    filename = f'{year}.csv'
    df = pd.read_csv(filename)
    df['year'] = year
    dataframes.append(df)
combined_df = pd.concat(dataframes)

# Sort the DataFrame by country and year
combined_df = combined_df.sort_values(['country', 'year'])

# Convert the Earning column to numeric values
combined_df['earning'] = combined_df['earning'].str.replace('[\$,]', '', regex=True).astype(float)

# Calculate the percentage change of earnings for each country
combined_df['earning_percentage_change'] = combined_df.groupby('country')['earning'].pct_change() * 100

# Create the line graph with Plotly
fig = go.Figure()

for country in combined_df.sort_values('rank')['country'].unique():
    country_data = combined_df[combined_df['country'] == country]
    fig.add_trace(go.Scatter(
        x=country_data['year'],
        y=country_data['earning_percentage_change'],
        mode='lines',
        name=str(country),
        text=[country] * len(country_data['year']),
        hovertemplate='Country: %{text}<br>Year: %{x}<br>Earning % Change: %{y:.2f}%',
        line=dict(shape='spline', smoothing=1),
    ))

# Customize the layout of the graph
fig.update_layout(
    xaxis_title='Year',
    yaxis_title='Earning % Change',
    hovermode='closest',
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(color='white'),
    showlegend=False,
)

fig.update_traces(hoverlabel_namelength=0)

# Show the graph
#pio.write_html(fig, 'earningPercentageChangeByCountryPE.html')
#offline.plot(fig, filename='EarningPercentageChangePigeonEffect.html', auto_open=False)
pio.show(fig)