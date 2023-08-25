import csv
import os
import plotly.express as px
import plotly.io as pio


def plot_bar_chart(sorted_ranks):
    countries = [item[0] for item in sorted_ranks]
    ranks = [item[1] for item in sorted_ranks]

    # Calculate the difference from the worst rank for each country
    worst_rank = max(ranks)
    diff_ranks = [worst_rank - rank for rank in ranks]

    fig = px.bar(x=countries[:30], y=diff_ranks[:30], orientation='v')
    fig.update_layout(
        xaxis_title='Country',
        yaxis_title='Inverted Average Ranks',
        font=dict(size=7, color='white'),  # Set font size for country names
        plot_bgcolor='black',  # Set background color to black
        paper_bgcolor='black',
    )

    # Add colorbar
    fig.update_traces(
        marker=dict(
            color=diff_ranks[:30],
            colorscale='Viridis',
            colorbar=dict(title='Inverted Average Ranks')
        ),
        customdata=ranks[:30],
        hovertemplate='<b>%{x}</b><br>Average Rank: %{customdata:.2f}',
    )

    fig.show()
    pio.write_html(fig, 'averageRanks.html')


def calculate_average_rank(folder_path, output_file):
    nation_ranks = {}

    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            with open(os.path.join(folder_path, filename), 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # Skip the header row
                for row in reader:
                    rank_str = row[1]
                    nation = row[2]

                    rank = int(rank_str.replace('.', ''))  # Remove dot from rank

                    if nation not in nation_ranks:
                        nation_ranks[nation] = []

                    nation_ranks[nation].append(rank)

    for nation, ranks in nation_ranks.items():
        if len(ranks) == 0:
            ranks.append(len(os.listdir(folder_path)) + 1)  # Assign last position for missing countries

    average_ranks = {}
    for nation, ranks in nation_ranks.items():
        average_rank = sum(ranks) / len(ranks)
        average_ranks[nation] = average_rank

    sorted_ranks = sorted(average_ranks.items(), key=lambda x: x[1])  # Sort the average ranks in ascending order

    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Country', 'Average Rank'])
        for nation, rank in sorted_ranks:
            writer.writerow([nation, rank])


# Example usage
csv_folder = 'fightingGames'  # Pfad zum Ordner mit CSV-Dateien
output_file = 'averageRanksBattleCollectibleCardfightingGames.csv'

calculate_average_rank(csv_folder, output_file)

# Load the sorted ranks from the output CSV file
with open(output_file, 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    sorted_ranks = [(row[0], float(row[1])) for row in reader]

# Plot the bar chart
plot_bar_chart(sorted_ranks)
