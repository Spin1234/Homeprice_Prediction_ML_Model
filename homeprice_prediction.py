import pandas as pd
import numpy as np
from sklearn import linear_model
import joblib

df = pd.read_csv("homeprices.csv")
print(df.head())
model = linear_model.LinearRegression()
model.fit(df[['area']],df.price)
print(model.predict([[5000]]))
print(model.coef_)
print(model.intercept_)

#Save Trained Model Using joblib
joblib.dump(model, 'model_predict_homeprice')
ml = joblib.load('model_predict_homeprice')
print(ml.predict([[5000]]))
