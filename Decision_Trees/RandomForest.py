import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier


#Reading the PastHires.csv file (I/P) Training set
input_file = "PastHires.csv"
df = pd.read_csv(input_file, header = 0)

# Since scikit-learn wants numerical data, convert all categorical data to numerical

d = {'Y': 1, 'N': 0}
df['Hired'] = df['Hired'].map(d)
df['Employed?'] = df['Employed?'].map(d)
df['Top-tier school'] = df['Top-tier school'].map(d)
df['Interned'] = df['Interned'].map(d)
d = {'BS': 0, 'MS': 1, 'PhD': 2}
df['Level of Education'] = df['Level of Education'].map(d)
df.head()

#Assigning features from column 1 to 5, because 'Hired' is the item we want to predict.
features = list(df.columns[:6])

y = df["Hired"]
X = df[features]
f = open("resultss1", "w+")

for i in range(100):
    clf = RandomForestClassifier(n_estimators=10)
    clf = clf.fit(X, y)
    f.write(str(clf.predict([[10, 1, 4, 0, 0, 0]])))
    f.write (str(clf.predict([[10, 0, 4, 0, 0, 0]])))
    f.write('\n')

#Predict employment of an employed 10-year veteran
print (clf.predict([[10, 1, 4, 0, 0, 0]]))
#...and an unemployed 10-year veteran
print (clf.predict([[10, 0, 4, 0, 0, 0]]))

