import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL der Website
url = 'https://www.speedtest.net/global-index'
# Die Tabelle scrappen
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find_all('table', class_='list-results')[0]
rows = table.find_all('tr', class_='data-result results')


# Daten extrahieren und in eine Liste speichern
data = []
for row in rows:
    cells = row.find_all('td')
    rank = cells[0].text.strip()
    country = cells[2].text.strip()
    averageBroadbandDownloadSpeed = cells[3].text.strip()
    data.append([rank, country, averageBroadbandDownloadSpeed])

# Liste in einen Pandas DataFrame konvertieren
df = pd.DataFrame(data, columns=['rank', 'country', 'average Broadband Download Speed'])

print(df)


# Liste als csv speichern
df.to_csv('averageInternetSpeedMobile.csv', index=False)