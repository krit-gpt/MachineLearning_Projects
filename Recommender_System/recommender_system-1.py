import pandas as pd
import numpy as np

# Reading in the data from the csv files
r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('ml-100k/u.data', sep='\t', names=r_cols, usecols=range(3), encoding="ISO-8859-1")

m_cols = ['movie_id', 'title']
movies = pd.read_csv('ml-100k/u.item', sep='|', names=m_cols, usecols=range(2), encoding="ISO-8859-1")

#merging both the tables with a natural join
ratings = pd.merge(movies, ratings)

#print(ratings.head())
# Magical pandas command that makes a mtrix of every movie nad every user and all the ratings that every user gave to every movie
movieRatings = ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')

# For item based collaborative filtering, we need to find the correlation amongst the columns

starWarsRatings = movieRatings['Star Wars (1977)']

#Correlate each column with every other column in the dataframe
similarMovies = movieRatings.corrwith(starWarsRatings)
similarMovies = similarMovies.dropna()
df = pd.DataFrame(similarMovies)

# will group ratings by title and aggregate ratings with average; just to have a look
movieStats = ratings.groupby('title').agg({'rating': [np.size, np.mean]})

# Adding a basic confidence level of 100 people as the minimum bound
# so that, only those movies which have more than 100 ratings are shown, rest are rejected
popularMovies = movieStats['rating']['size'] >= 100

f = open("resultss.txt", "w+")

#Joining two dataframes to get the results
df1 = movieStats[popularMovies].join(pd.DataFrame(similarMovies, columns=['similarity']))
# sort the results by the similarity column
print(df1.sort_values(['similarity'], ascending=False)[:15])
f.write(str(df1.sort_values(['similarity'], ascending=False)[:15]))