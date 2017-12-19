The project was done as part of the online course on Udemy on Recommender Systems. The data used is real Movie Recommendation data taken from - grouplens.org. The first 100,000 ratings have been taken for the project.
Techniques and skills that are implemented in the project are:
	Item Based Collaborative Filtering
	pivot_table in Pandas
	
There are two scripts in the Project.
The first one produces recommendations based on the similarity to a particular movie - ‘Star Wars’ in this case.
The second one is a full blown recommendation system that produces recommendations for a particular user based on their entire history of ratings.

The minimum confidence level is taken to be 100 ratings.
For script-1, we throw out the movies which have less than 100 ratings. For the script-2, we throw out the movies which have not been rated by atleast 100 same users. 

The results are presented in the results_script1.txt for script-1 and results-script2.txt for the second script.