import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

data = pd.read_csv('EV-Data.csv')
df = data[(data['parameter'] == 'EV sales') & (data['unit'] == 'Vehicles')]
df = df[['year', 'value']].dropna()

X = df['year'].values.reshape(-1, 1)
y = df['value'].values

poly = PolynomialFeatures(degree=3, include_bias=False)

X_poly = poly.fit_transform(X)

poly_reg_model = LinearRegression()
poly_reg_model.fit(X_poly, y)

future_year = np.array([[2020]])
future_year_poly = poly.transform(future_year)
future_prediction = poly_reg_model.predict(future_year_poly)

print(f"Predicted EV sales for 2040: {future_prediction[0]:.2f}")