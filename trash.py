import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests


def generate_offense():
    url = "https://www.pro-football-reference.com/years/2020/scrimmage.htm"
    data = requests.get(url).text
    soup = BeautifulSoup(data, 'html.parser')
    tbody = soup.find('tbody')

    categories = ['player', 'team', 'targets', 'rec', 'rec_yds', 'rec_yds_per_rec',
                  'rec_td', 'rec_first_down', 'rec_per_g', 'rec_yds_per_g', 'catch_pct',
                  'rec_yds_per_tgt', 'rush_att', 'rush_yds', 'rush_td', 'rush_first_down',
                  'rush_yds_per_att', 'rush_yds_per_g', 'rush_att_per_g', 'touches',
                  'yds_per_touch', 'yds_from_scrimmage', 'rush_receive_td', 'fumbles']

    rows = []
    for i in soup.find_all('tr'):
        row = []
        for j in i.find_all('td'):
            if j.attrs['data-stat'] in categories:
                row.append(j.text.strip())
        if len(row) != 0:
            rows.append(row)

    df = pd.DataFrame(data=rows, columns=categories)
    df.to_csv('data/2020_week_4_player_totals.csv', encoding='utf-8')


generate_offense()
