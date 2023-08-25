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

# Calculate the total earnings per year for all countries
total_earnings_per_year = combined_df.groupby('year')['earning'].sum()

# Create the line graph with Plotly
fig = go.Figure(data=[go.Scatter(x=total_earnings_per_year.index, y=total_earnings_per_year, mode='lines')])

# Customize the layout of the graph
fig.update_layout(
    xaxis_title='Year',
    yaxis_title='Total Earnings',
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(color='white'),
)

# Apply smoothing to the line
fig.update_traces(line=dict(shape='spline', smoothing=1))
fig.update_traces(hovertemplate='Year: %{x}<br>Total Earnings: $%{y:,.2f}')
fig.update_traces(hoverlabel_namelength=0)

# Show the graph
pio.write_html(fig, 'totalYearlyEarningsPE.html')
pio.show(fig)
