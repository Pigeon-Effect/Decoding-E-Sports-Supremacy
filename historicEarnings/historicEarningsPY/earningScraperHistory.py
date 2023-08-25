import requests
from bs4 import BeautifulSoup

url = 'https://www.esportsearnings.com/games/browse-by-genre'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find_all('div', class_='games_main_genre_body')

for row in table:
    country = table.find_all(''[1].text.strip()
    totalMedals = cols[6].text.strip()

df = pd.DataFrame(table_data, columns=["Country", "Number of medals"])
df.to_csv('gameHrefsGenreRanking.csv', index=False)