import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests


def generate_csv(type, year, categories):
    url = "https://www.pro-football-reference.com/years/" + year + "/" + type + ".htm"
    data = requests.get(url).text
    soup = BeautifulSoup(data, 'html.parser')
    tbody = soup.find('tbody')

    rows = []
    for i in tbody.find_all('tr'):
        row = []
        for j in i.find_all('td'):
            if j.attrs['data-stat'] in categories:
                row.append(j.text.strip())
        if len(row) != 0:
            rows.append(row)

    df = pd.DataFrame(data=rows, columns=categories)
    df.to_csv('data/' + year + type + '_player_totals.csv', encoding='utf-8')

offense_categories = ['player', 'team', 'targets', 'rec', 'rec_yds', 'rec_yds_per_rec',
                  'rec_td', 'rec_first_down', 'rec_per_g', 'rec_yds_per_g', 'catch_pct',
                  'rec_yds_per_tgt', 'rush_att', 'rush_yds', 'rush_td', 'rush_first_down',
                  'rush_yds_per_att', 'rush_yds_per_g', 'rush_att_per_g', 'touches',
                  'yds_per_touch', 'yds_from_scrimmage', 'rush_receive_td', 'fumbles']

defense_categories = ['team', 'points', 'total_yards', 'plays_offense', 'yds_per_play_offense',
                  'turnovers', 'fumbles_lost', 'first_down', 'pass_cmp', 'pass_att', 'pass_yds', 
                  'pass_td', 'pass_int', 'pass_net_yds_per_att', 'pass_fd', 'rush_att', 'rush_yds',
                  'rush_td', 'rush_yds_per_att', 'rush_fd', 'penalties', 'penalties_yds', 'pen_fd',
                  'score_pct', 'turnover_pct', 'exp_pts_def_tot']

generate_csv("scrimmage", "2020", offense_categories)
generate_csv("opp", "2020", defense_categories)