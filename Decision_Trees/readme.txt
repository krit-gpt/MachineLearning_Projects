The project was done to understand the concepts of:
Entropy - The randomness in the data 
Decision Trees - construct a flowchat to help decide a classification
ID3 Algorithm (done through the in-built function in scikit-learn)
Random Forest - to avoid the problem of ‘overfitting’ - Bootstrap Aggregating/Bagging. 

The program is trained on a past data of whether a candidate was hired for the job or not based on the parameters such as - 
Number of years of experience
Level of Education - BS, MS, PhD
Whether the candidate is from a top-tier school or not
If he did an internship
etc

Since scikit-learn wants numerical data, the categorical data is divided into numerical form first and then Decision Tree is made.

Gini-Score at each level measures the entropy at each level. 

Another aspect of the project is to learn about Random Forests - hence, 10 trees in random forest are made and the data, after being trained, is tested to predict two sample cases.
The result is repeated 100 times. It can be clearly seen that the data is not consistent. Maybe 10 trees for the forest are not enough!
The results are in the results.txt file.

