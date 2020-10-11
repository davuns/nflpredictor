import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests


def generate_csv(type, year, categories):
    url = "https://www.pro-football-reference.com/years/" + str(year) + "/" + type + ".htm"
    url_data = requests.get(url).text
    bs = BeautifulSoup(url_data, 'html.parser')
    tbody = bs.find('tbody')

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

def generate_box_scores_list(year):
    url = "https://www.pro-football-reference.com/years/" + str(year) + "/games.htm"
    url_data = requests.get(url).text
    bs = BeautifulSoup(url_data, 'html.parser')
    tbody = bs.find('tbody')

    box_scores_list = []
    for i in tbody.find_all('tr'):
        for j in i.find_all('td'):
            if j.attrs['data-stat'] == 'boxscore_word':
                if j.find('a') != None:
                    box_scores_list.append('https://www.pro-football-reference.com' + j.find('a').attrs['href'])

    return box_scores_list