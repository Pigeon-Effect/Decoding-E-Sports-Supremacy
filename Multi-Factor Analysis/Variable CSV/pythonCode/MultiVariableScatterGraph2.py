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

colors = ['#05f9e2', '#08FF08', '#FF0883', '#B30059', '#77DD77', '#C4D300', '#E0E722', '#FDB813', '#FFA400', '#E40046', '#00BCE3', '#1E8FD5', '#D6E865', '#800500']

for i, col in enumerate(numeric_columns):
    trace = (go.Scatter(
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
    # Set the default visibility of traces
    if col == 'Total E-Sports Earning':
        trace.visible = True
    else:
        trace.visible = 'legendonly'

    fig.add_trace(trace)

# Rotate the x-axis labels for better readability
fig.update_layout(
    xaxis=dict(tickangle=45, ticktext=[], tickvals=[]),
    xaxis_title='Country',
    yaxis_title='Normalized Value',
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(color='white'),
    height=700,  # Set the height to 100% of the screen
    showlegend=True,
    legend=dict(
        orientation='v',
        x=1.02,  # Position legend to the right of the graph
        y=0.5,  # Align legend with the top of the graph
        #xanchor='center',
        #yanchor='bottom',
        title_text=None,  # Remove the legend title
        title_font=dict(size=14),
        itemsizing='trace',  # To have fixed number of columns
        traceorder='normal',  # To maintain the order in which the traces were added
        itemclick='toggle',  # To show/hide data when clicking on legend items
        itemdoubleclick='toggleothers',  # To isolate data when double-clicking on legend items
        itemwidth=100,  # Adjust the width of each legend item for better alignment
    ),
    xaxis_range=[-1.1,len(sorted_data['Country'])+0.2],  # Set the x-axis range to cover all data points
)


config = {'scrollZoom': False}

fig.update_traces(hoverlabel_namelength=0)

# Show the graph
pio.write_html(fig, 'multiVariableScatterPlotPE.html', config=config)
pio.show(fig)
