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

#create new dictionary
games_played = [['Arsenal','4'], ['Aston Villa','3'], ['Brighton','4'], ['Burnley','3'], ['Chelsea','4'], ['Crystal Palace','4'], ['Everton','4'], ['Fulham','4'], ['Leicester','4'], ['Leeds','4'], ['Liverpool','4'], ['Man City','3'], ['Man Utd','3'], ['Newcastle','4'], ['Sheffield Utd','4'], ['Southampton','4'], ['Spurs','4'], ['West Brom','4'], ['West Ham','4'], ['Wolves','4']]
#turn into a DataFrame
played_df = pd.DataFrame(games_played,columns=['team','games_played'])
#overwrite existing DataFrame column
teams_df['played'] = played_df['games_played'].astype(str).astype(int)
#voila
print(teams_df.head())