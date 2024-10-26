import pandas as pd
import numpy as np

# Define the path to the CSV file
csv_file_path = '../data/CCFC_match_lineups_data.csv'

# Read the CSV file into a Pandas DataFrame
dataframe = pd.read_csv(csv_file_path)
pd.set_option('display.max_rows', None)

# Convert the DataFrame to a NumPy array
data_array = dataframe.to_numpy()

# Print the DataFrame and the NumPy array
#print("Pandas DataFrame:")
#print(dataframe[['opposition_team','location']])
home = 'home'
awayMatches = dataframe.query('location == "away"')
print(awayMatches[['opposition_team', 'location']])

print("\nNumPy Array:")
#print(data_array)
