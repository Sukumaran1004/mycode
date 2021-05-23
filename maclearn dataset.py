# importing library

import numpy as np
import matplotlib.pyplot
import pandas as pd

# import datasets
data=pd.read_csv('Data.csv')
x=data.iloc[:, :-1].values
y=data.iloc[:, -1].values
print(x)
print(y)


# taking care of missing data
from sklearn.impute import SimpleImputer
impute=SimpleImputer(missing_values=np.nan,strategy='mean')
impute.fit(x[:, 1:3])
x[:, 1:3]=impute.transform(x[:, 1:3])
print(x)






