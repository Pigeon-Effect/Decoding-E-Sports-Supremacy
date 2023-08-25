import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio

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

# Calculate the total earnings per year
total_earnings_per_year = combined_df.groupby('year')['earning'].sum()

# Normalize the earnings for each year
combined_df['earning_normalized'] = combined_df.apply(lambda row: row['earning'] / total_earnings_per_year[row['year']], axis=1)

# Create the stacked bar graph with Plotly
fig = go.Figure()

fluor_colors = ['#567CFF',
                '#8EA8FF',
                '#7A78FF',
                '#D875FF',
                '#8D4BE0',
                '#CCFF00',
                '#7FFF00',
                '#39FF14',
                '#1F51FF',
                '#0A4E43',
                '#029782',
                '#ABC65F',
                '#83018E',
                '#0D8596',
                '#B624C1',
                '#EF40FF',
                '#9457E4',
                '#1562C1',
                '#350B99',
                '#E923F4',
                '#72076E',
                '#12E195',
                '#0FF985',
                '#FDE802',
                '#FF901B',
                '#FC5E01',
                '#79FDF9',
                '#03EDF4',
                '#03CDFF',
                '#2368FB',
                '#5A32FC',
                '#D1FE49',
                '#FF1F4F',
                '#BE0357',
                '#017562',
                '#F5F232',
                '#5600F4'
                ]

def cycle_colors(colors):
    index = 0
    while True:
        yield colors[index]
        index = (index + 1) % len(colors)


color_iterator = cycle_colors(sorted(fluor_colors)[1:])

for country in combined_df.sort_values('rank')['country'].unique():
    country_data = combined_df[combined_df['country'] == country]
    color = next(color_iterator)
    fig.add_trace(go.Bar(
        x=country_data['year'],
        y=country_data['earning_normalized'],
        name=str(country),
        text=[country] * len(country_data['year']),
        hovertemplate='Country: %{text}<br>Year: %{x}<br>Earning: %{y:.2%}',
        textposition='inside',
        marker=dict(
            color=color
        )
    ))

# Customize the layout of the graph
fig.update_layout(
    xaxis_title='Year',
    yaxis_title='Normalized Earnings',
    barmode='stack',
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(color='white'),
    showlegend=False,
    height=700,  # Set the height to 100% of the screen
)

fig.update_traces(hoverlabel_namelength=0)

# Show the graph
pio.write_html(fig, 'splittedBarGraphNormalizedEarningsByCountryByYear#3.html')
pio.show(fig)
