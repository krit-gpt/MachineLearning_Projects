import pandas as pd


# Reading in the data
r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('ml-100k/u.data', sep='\t', names=r_cols, usecols=range(3), encoding="ISO-8859-1")

m_cols = ['movie_id', 'title']
movies = pd.read_csv('ml-100k/u.item', sep='|', names=m_cols, usecols=range(2), encoding="ISO-8859-1")

ratings = pd.merge(movies, ratings)
#print(ratings.head())

# Using the pivot_table pandas command to get the matrix of how we want it to be
userRatings = ratings.pivot_table(index=['user_id'],columns=['title'],values='rating')

# TO calculate teh correlation between every column pair in the matrix where in
# atleast 100 people have rated both the movies and using Pearson Correlation for the same
corrMatrix = userRatings.corr(method='pearson', min_periods=100)

# Adding a random user
myRatings = userRatings.loc[0].dropna()

simCandidates = pd.Series()
for i in range(0, len(myRatings.index)):
    print ("Adding sims for " + myRatings.index[i] + "...")
    # Retrieve similar movies to this one that I rated
    sims = corrMatrix[myRatings.index[i]].dropna()
    # Now scale its similarity by how well I rated this movie
    sims = sims.map(lambda x: x * myRatings[i])
    # Add the score to the list of similarity candidates
    simCandidates = simCandidates.append(sims)

simCandidates = simCandidates.groupby(simCandidates.index).sum()
#
simCandidates.sort_values(inplace = True, ascending = False)

f = open("results-script2.txt", "w+")

# Remove the movies already watched
filteredSims = simCandidates.drop(myRatings.index)
print(simCandidates.head(10))
f.write(simCandidates.head(10))