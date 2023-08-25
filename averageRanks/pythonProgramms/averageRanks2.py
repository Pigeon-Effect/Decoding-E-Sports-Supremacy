import csv
import plotly.express as px
import numpy as np


def plot_bar_chart(sorted_ranks):
    countries = [item[0] for item in sorted_ranks]
    ranks = [item[1] for item in sorted_ranks]

    # Calculate the difference from the worst rank for each country
    worst_rank = max(ranks)
    diff_ranks = [worst_rank - rank for rank in ranks]

    fig = px.bar(x=countries, y=diff_ranks, orientation='v')
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
            color=diff_ranks,
            colorscale='Viridis',
            colorbar=dict(title='Inverted Average Ranks')
        ),
        customdata=ranks,
        hovertemplate='<b>%{x}</b><br>Average Rank: %{customdata:.2f}',
        )

    fig.show()


def calculate_average_rank(csv_files, output_file):
    nation_ranks = {}

    for file in csv_files:
        with open(file, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip the header row
            for row in reader:
                rank_str = row[0]
                nation = row[1]

                rank = int(rank_str.replace('.', ''))  # Remove dot from rank

                if nation not in nation_ranks:
                    nation_ranks[nation] = []

                nation_ranks[nation].append(rank)

    for nation, ranks in nation_ranks.items():
        if len(ranks) == 0:
            ranks.append(len(csv_files) * 170 + 1)  # Assign last position for missing countries

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
csv_files = [
    'ageOfEmpires2.csv',
    'ageOfEmpires4.csv',
    'apexLegends.csv',
    'arenaOfValor.csv',
    'assettoCorsa.csv',
    'autoChess.csv',
    'brawlhalla.csv',
    'brawlStars.csv',
    'chess24.csv',
    'chessCom.csv',
    'clashOfClans.csv',
    'clashRoyale.csv',
    'codAdvancedWarefare.csv',
    'codBlackObs2.csv',
    'codBlackOps3.csv',
    'codBlackOps4.csv',
    'codBlackOpsColdWar.csv',
    'codGhosts.csv',
    'codInfiniteWarfare.csv',
    'codMobile.csv',
    'codModernWarfare.csv',
    'codModernWarfare2.csv',
    'codModernWarfare3.csv',
    'codVanguard.csv',
    'CODWarzone.csv',
    'codWW2.csv',
    'counterStrike.csv',
    'counterStrikeSource.csv',
    'crossFire.csv',
    'crossfireMobile.csv',
    'csgo.csv',
    'dota2.csv',
    'fifa17.csv',
    'fifa18.csv',
    'fifa19.csv',
    'fifa20.csv',
    'fifa21.csv',
    'fifa22.csv',
    'fifa23.csv',
    'fifaOnline3.csv',
    'fifaOnline4.csv',
    'fortnite.csv',
    'freeFire.csv',
    'gears5.csv',
    'gearsOfWar.csv',
    'gwent.csv',
    'h1z1.csv',
    'halo2.csv',
    'halo3.csv',
    'halo5Guardians.csv',
    'haloInfinite.csv',
    'hearthstone.csv',
    'hereosOfNewerth.csv',
    'heroesOfTheStorm.csv',
    'identity5.csv',
    'iRacingCom.csv',
    'liChess.csv',
    'lol.csv',
    'lolWildRift.csv',
    'maddenNfl17.csv',
    'maddenNfl20.csv',
    'maddenNfl22.csv',
    'magicTheGatheringArena.csv',
    'magicTheGatheringOnline.csv',
    'minecraft.csv',
    'mobileLegendsBangBang.csv',
    'narakaBladepoint.csv',
    'nba2k18.csv',
    'overwatch.csv',
    'overwatch2.csv',
    'painkiller.csv',
    'paladins.csv',
    'playerunknownsBattleground.csv',
    'playerunknownsBattlegroundMobile.csv',
    'pointBlank.csv',
    'quake3Arena.csv',
    'quakeChampions.csv',
    'rainbowSixSiege.csv',
    'rFactor2.csv',
    'rocketLeague.csv',
    'shadowVerse.csv',
    'smite.csv',
    'starCraft2.csv',
    'starcraftBroodWar.csv',
    'starcraftRemastered.csv',
    'streetFighter5.csv',
    'streetFighter5ArcadeEdition.csv',
    'streetFightert5ChampionEdition.csv',
    'superSmashBrosMelee.csv',
    'superSmashBrosUltimate.csv',
    'superSmashBrosWiiU.csv',
    'teamFightTactics.csv',
    'tekken7.csv',
    'turboRacingLeague.csv',
    'vainGlory.csv',
    'valorant.csv',
    'warcraft3.csv',
    'warcraft3Reforged.csv',
    'worldOfTanks.csv',
    'wow.csv'
]

output_file = 'average_ranks.csv'

calculate_average_rank(csv_files, output_file)

# Load the sorted ranks from the output CSV file
with open(output_file, 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    sorted_ranks = [(row[0], float(row[1])) for row in reader]

# Plot the bar chart
plot_bar_chart(sorted_ranks)

pio.write_html(fig, 'averageRanksPE#1.html')
