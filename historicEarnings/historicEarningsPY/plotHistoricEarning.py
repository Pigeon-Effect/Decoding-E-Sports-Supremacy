import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio

# Load the CSV files and concatenate them into a single DataFrame
dataframes = []
years = range(2014, 2024)
for year in years:
    filename = f'earnings{year}.csv'
    df = pd.read_csv(filename)
    df['year'] = year
    dataframes.append(df)
combined_df = pd.concat(dataframes)

# Sort the DataFrame by country and year
combined_df = combined_df.sort_values(['country', 'year'])

# Convert the Earning column to numeric values
combined_df['earning'] = combined_df['earning'].str.replace('[\$,]', '', regex=True).astype(float)

# Create the line graph with Plotly
fig = go.Figure()

for country in combined_df[combined_df['year'] == 2023].sort_values('rank')['country'].unique():
    country_data = combined_df[combined_df['country'] == country]
    fig.add_trace(go.Scatter(
        x=country_data['year'],
        y=country_data['earning'],
        mode='lines',
        name=str(country),
        hovertemplate='country: %{name}<br>year: %{x}<br>earning: %{y:,.2f}',
        line=dict(shape='spline', smoothing=1),
    ))

# Customize the layout of the graph
fig.update_layout(
    title='earnings of countries over time',
    xaxis_title='year',
    yaxis_title='earning',
    hovermode='closest',
)

# Show the graph
pio.show(fig)
