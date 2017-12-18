import numpy as np
import pandas as pd
from sklearn import tree
#Header files needed for displaying the data
from IPython.display import Image
from sklearn.externals.six import StringIO
import pydotplus

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

#Calling the Decision Tree inbuilt-function
y = df["Hired"]
X = df[features]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,y)

#To display the data
dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data,
                         feature_names=features)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
Image(graph.create_png())



