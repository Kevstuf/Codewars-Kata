# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 15:42:33 2020

@author: kevst
"""

#Scrape top 500 users of Codewars

import requests
from bs4 import BeautifulSoup

url = "https://www.codewars.com/users/leaderboard"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
main_table = soup.find("table")
rows = main_table.find_all("tr")

#Not working. Need to extract username, clan, and honor
for row in rows:
    #print(row, end = "\n\n")
    user = row.find_all("a")
    print(user)
