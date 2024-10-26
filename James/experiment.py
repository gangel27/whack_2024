import pandas as pd
import numpy as np

# Define the path to the CSV file
csv_file_path = './CCFC_match_lineups_data.csv'

# Read the CSV file into a Pandas DataFrame
dataframe = pd.read_csv(csv_file_path)
pd.set_option('display.max_rows', None)

# Convert the DataFrame to a NumPy array
data_array = dataframe.to_numpy()

# Print the DataFrame and the NumPy array
#print("Pandas DataFrame:")
#print(dataframe.head())
print(dataframe['opposition_team'].dropna().nunique())
home = 'home'
#awayMatches = dataframe.query('location == "away"')
#print(dataframe[['opposition_team']])
#print("\nNumPy Array:")
#print(data_array)
