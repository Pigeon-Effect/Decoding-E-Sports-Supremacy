import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the Wikipedia page
url = "https://www.cisco.com/c/m/en_us/about/corporate-social-responsibility/research-resources/digital-readiness-index.html#/"

# Send an HTTP GET request to the URL and fetch the HTML content
response = requests.get(url)
html_content = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")
print(soup)
table = soup.find("tbody")
print(table)

if table:
    data_rows = table.find_all("tr")
    print(data_rows)
    table_data = []
    for row in data_rows:
        cols = row.find_all(["td"])  # Use "th" and "td" both for extracting data from header and data cells
        print(cols)
        country = cols[1].text.strip()
        totalMedals = cols[6].text.strip()  # Extract the text from the <a> tag within the third column (Country)


        table_data.append([country, totalMedals])  # Append data as a list

    # Create a DataFrame using pandas
    df = pd.DataFrame(table_data, columns=["Country", "Number of medals"])

    # Print the DataFrame
    print(df)

    # Save df to CSV File
    #csv_filename = "historicTableOfOlympicMedals.csv"
    #df.to_csv(csv_filename, index=False)
'''