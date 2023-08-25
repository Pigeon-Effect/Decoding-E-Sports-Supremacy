import csv
import unicodedata

def replace_non_utf8_characters(input_file, output_file):
    def replace_character(c):
        try:
            return c.encode('utf-8').decode('utf-8')
        except UnicodeEncodeError:
            normalized_c = unicodedata.normalize('NFKD', c)
            ascii_c = ''.join([char for char in normalized_c if ord(char) < 128])
            return ascii_c

    with open(input_file, 'r', newline='', encoding='utf-8') as infile, \
            open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            cleaned_row = [replace_character(cell.replace(':', '')) for cell in row]
            writer.writerow(cleaned_row)

# Beispielaufruf
input_file = 'moba.csv'  # Eingabedatei im CSV-Format
output_file = 'cleanMOBA.csv'  # Ausgabedatei mit bereinigten Zeichen

replace_non_utf8_characters(input_file, output_file)
