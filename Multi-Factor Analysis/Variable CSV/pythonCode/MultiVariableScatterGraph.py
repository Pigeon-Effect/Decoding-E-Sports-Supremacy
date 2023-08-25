import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio

# Read the CSV file
input_file = 'MulitFactorTable#8.csv'
data = pd.read_csv(input_file, delimiter=';')

# Get the numeric columns (excluding the first column with country names)
numeric_columns = data.columns[1:]

# Convert the numeric values to float
data[numeric_columns] = data[numeric_columns].replace({',': '.'}, regex=True).astype(float)

# Normalize the data
normalized_data = (data.iloc[:, 1:] - data.iloc[:, 1:].min()) / (data.iloc[:, 1:].max() - data.iloc[:, 1:].min())

# Add the country column back to the normalized data
normalized_data.insert(0, 'Country', data['Country'])

# Sort the data by the value in the 5th column (E-Sports Earnings)
sorted_data = normalized_data.sort_values(by=[numeric_columns[0], 'Country'])

sorted_but_not_normalized = data.sort_values(by=[numeric_columns[0], 'Country'])

# Calculate the rolling mean for each column (window size = 10)
rolling_mean_data = sorted_data.rolling(window=10, min_periods=1, axis=0).mean()

# Create the Scatter Plot
fig = go.Figure()

hover_formats = {
    'Total E-Sports Earning': 'Total E-Sports Earning: $%{customdata:,.2f}',
    'Average Broadband Internetspeed': 'Average Broadband Internet Speed: %{customdata:.2f} Mbps',
    'Average mobile Internetspeed': 'Average mobile Internet Speed: %{customdata:.2f} Mbps',
    'Digital Competetiveness Index': 'Digital Competetiveness Index: %{customdata:.0f}',
    'Freedome House Index': 'Freedom House Index: %{customdata:.0f}',
    'Inverted Gender Inequality Index': 'Gender Inequality Index: %{customdata:.2f}',
    'Human Development Index': 'Human Development Index: %{customdata:.2f}',
    'Internet Freedome Index': 'Internet Freedom Index: %{customdata:.2f}',
    'Nominal GDP': 'Nominal GDP: %{customdata:,.0f},000',
    'Total Olympic Medals': 'Total Olympic Medals: %{customdata:.0f}',
    'PPP GDP': 'PPP GDP: $%{customdata:,.0f},000',
    'PPP GDP per Capita': 'PPP GDP per Capita: $%{customdata:,.0f},000',
    'Population': 'Population: %{customdata:,.0f}',
}

colors = ['blue', 'green', 'red', 'purple', 'orange', 'yellow', 'pink', 'brown', 'gray', 'cyan', 'magenta', 'lime', 'fuchsia', 'navy']


for i, col in enumerate(numeric_columns):
    fig.add_trace(go.Scatter(
        x=sorted_data['Country'],
        y=sorted_data[col],
        mode='markers',
        name=col,
        marker=dict(
            size=8,
            color=colors[i],  # Use a different color for each column
            colorscale='Viridis',
            showscale=False
        ),
        customdata=sorted_but_not_normalized[[col]],
        hovertemplate='<b>%{x}</b><br>' + hover_formats[col],
    ))

    # Add the smoothed line
    fig.add_trace(go.Scatter(
        x=sorted_data['Country'],
        y=rolling_mean_data[col],
        mode='lines',
        line=dict(color=colors[i], width=1),  # Adjust the width if needed
        showlegend=False,
        hoverinfo='skip',
        visible='legendonly',   # Start with the moving averages hidden
    ))

# Rotate the x-axis labels for better readability
fig.update_layout(
    xaxis=dict(tickangle=90, tickfont=dict(size=8)),
    xaxis_title='Country',
    yaxis_title='Normalized Value',
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(color='white'),
    height=800,
    showlegend=True,
)

fig.update_traces(hoverlabel_namelength=0)

# Show the graph
pio.show(fig)
