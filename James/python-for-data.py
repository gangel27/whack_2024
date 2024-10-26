#Notebook Config
import requests
import pandas as pd
import numpy as np
#matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('ggplot')
#API Set-Up
url = 'https://fantasy.premierleague.com/api/bootstrap-static/'
r = requests.get(url)
json = r.json()

elements_df = pd.DataFrame(json['elements'])
element_types_df = pd.DataFrame(json['element_types'])
teams_df = pd.DataFrame(json['teams'])

main_df = elements_df[['web_name','first_name','team','element_type','now_cost','selected_by_percent','transfers_in','transfers_out','form','event_points','total_points','bonus','points_per_game','value_season','minutes','goals_scored','assists','ict_index','clean_sheets','saves']]

print(element_types_df.head())
print(teams_df.head())