import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL der Website
url = 'https://www.esportsearnings.com/games/642-street-fighter-v-champion-edition' + '/countries'
# Die Tabelle scrappen
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table', class_='detail_list_table')
rows = table.find_all('tr', class_='format_row highlight')


# Daten extrahieren und in eine Liste speichern
data = []
for row in rows:
    cells = row.find_all('td')
    rank = cells[0].text.strip()
    country = cells[1].text.strip()
    earnings = cells[2].text.strip()
    players = cells[3].text.strip()
    data.append([rank, country, earnings, players])

# Liste in einen Pandas DataFrame konvertieren
df = pd.DataFrame(data, columns=['rank', 'country', 'earning', 'players'])

print(df)


# Liste als csv speichern
df.to_csv('streetFightert5ChampionEdition.csv', index=False)