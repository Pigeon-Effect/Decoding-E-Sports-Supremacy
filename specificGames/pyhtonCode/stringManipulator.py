import csv

def modify_countries(csv_file):
    updated_rows = []
    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) > 0:
                country = row[0]
                if country == 'Korea' or country == 'Korea, Republic of':
                    country = 'South Korea'
                elif country == 'Taiwan, Republic of China':
                    country = 'Taiwan'
                elif country == 'Viet Nam':
                    country = 'Vietnam'
                elif country == 'Macedonia':
                    country = 'North Macedonia'
                elif country == 'Iran, Islamic Republic of':
                    country = 'Iran'
                elif country == 'Syrian Arab Republic':
                    country = 'Syria'
                row[0] = country
            updated_rows.append(row)

    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(updated_rows)

# Beispielaufruf der Funktion
modify_countries('deine_datei.csv')
