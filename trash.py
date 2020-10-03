import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

def generate_season():
    url = "https://www.pro-football-reference.com/years/2020/scrimmage.htm"
    soup = BeautifulSoup(url, 'html.parser')
    print(soup.prettify())