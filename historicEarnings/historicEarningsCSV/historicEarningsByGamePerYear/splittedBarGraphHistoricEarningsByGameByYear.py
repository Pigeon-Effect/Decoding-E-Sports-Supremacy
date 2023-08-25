import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio

# Load the CSV files and concatenate them into a single DataFrame
dataframes = []
years = range(1998, 2023)
for year in years:
    filename = f'games_{year}.csv'
    df = pd.read_csv(filename)
    df['year'] = year
    dataframes.append(df)
combined_df = pd.concat(dataframes)

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


# Sort the DataFrame by country and year
combined_df = combined_df.sort_values(['country', 'year'])

# Convert the Earning column to numeric values
combined_df['earning'] = combined_df['earning'].str.replace('[\$,]', '', regex=True).astype(float)

# Group by year and game, calculate the sum of earnings
grouped_df = combined_df.groupby(['year', 'country'])['earning'].sum().reset_index()

# Normalize the earnings for each year
grouped_df['earning_normalized'] = grouped_df.groupby('year')['earning'].transform(lambda x: x / x.sum())

# Sort the games within each year by earning_normalized in descending order
grouped_df = grouped_df.sort_values(['year', 'earning_normalized'], ascending=[True, False])

def cycle_colors(colors):
    index = 0
    while True:
        yield colors[index]
        index = (index + 1) % len(colors)

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))

def distance_between_colors(color1, color2):
    r1, g1, b1 = hex_to_rgb(color1)
    r2, g2, b2 = hex_to_rgb(color2)
    return (r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2

def sort_colors_by_similarity(hex_colors):
    sorted_colors = [hex_colors[0]]
    hex_colors.remove(hex_colors[0])

    while hex_colors:
        last_color = sorted_colors[-1]
        nearest_color = min(hex_colors, key=lambda color: distance_between_colors(last_color, color))
        sorted_colors.append(nearest_color)
        hex_colors.remove(nearest_color)

    return sorted_colors

color_iterator = cycle_colors(sort_colors_by_similarity(fluor_colors))

# Create the stacked bar chart with Plotly
fig = go.Figure()

for game in grouped_df['country'].unique():
    game_data = grouped_df[grouped_df['country'] == game]
    color = next(color_iterator)
    fig.add_trace(go.Bar(
        x=game_data['year'],
        y=game_data['earning_normalized']*100,
        name=str(game),
        text=[game] * len(game_data['year']),
        hovertemplate='Game: %{text}<br>Year: %{x}<br>Earning: %{y:,.2f}%',
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
)

fig.update_traces(hoverlabel_namelength=0)

# Show the graph
pio.write_html(fig, 'splittedBarGraphHistoricEarningsByGameByYear#1.html')
pio.show(fig)
