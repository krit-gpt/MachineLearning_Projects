import pandas as pd
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

df = pd.read_excel('cars.xls')

f = open("results.txt", "w+")

# Choosing only three parameters from the I/P data
X = df[['Mileage', 'Cylinder', 'Doors']]
y = df['Price']

#normalises the results in the range of [-1,1] in order to carry out the analysis
X[['Mileage', 'Cylinder', 'Doors']] = scale.fit_transform(X[['Mileage', 'Cylinder', 'Doors']].as_matrix())

f.write(str(X))

est = sm.OLS(y, X).fit() # OLS - Ordinary Least Square for Multivariate Regression

f.write(str(est.summary()))



