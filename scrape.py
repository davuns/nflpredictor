import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests


def generate_csv(type, year, categories):
    url = "https://www.pro-football-reference.com/years/" + str(year) + "/" + type + ".htm"
    data = requests.get(url).text
    soup = BeautifulSoup(data, 'html.parser')
    tbody = soup.find('tbody')

    rows = []
    for i in tbody.find_all('tr'):
        row = []
        for j in i.find_all('td'):
            if j.attrs['data-stat'] == 'player':
               row.append(j.find('a').text.strip())
            elif j.attrs['data-stat'] in categories:
                row.append(j.text.strip())
        if len(row) != 0:
            rows.append(row)

    df = pd.DataFrame(data = rows, columns = categories)
    df.to_csv('data/' + str(year) + type + '_player_totals.csv', encoding='utf-8')