# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("resources/netflix_data.csv")


# Start coding here! Use as many cells as you like
import numpy as np
# print(netflix_df)
#to find the most frequent movie in 1990
movie_type_df =netflix_df[netflix_df['type'] == 'Movie']
movie_1990_df = movie_type_df[np.logical_and(movie_type_df['release_year'] >= 1990, movie_type_df['release_year'] <= 1999)]
# print(movie_1990['release_year'])
duration = int(movie_1990_df['duration'].mode()[0]) # 88
print(duration)

# to find the number of short movies released in 1990
action_df =  netflix_df[netflix_df['genre'] == 'Action']
# short_action_df =action_df[action_df['duration'] < 90]

short_action_movie_df = action_df[
    (action_df['duration'] < 90) &
    (action_df['type'] == 'Movie') &
    (action_df['release_year'] >= 1990) &
    (action_df['release_year'] <= 1999)
]


# print(short_action_movie_df.loc[:,['type', 'release_year' ,'duration' ,'genre']])
short_movie_count = len(short_action_movie_df)
print(short_action_movie_df.columns)