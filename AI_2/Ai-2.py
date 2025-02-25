import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


data = pd.read_csv('EV-Data.csv')


print("Dataset Preview:")
print(data.head())


df = data[(data['parameter'] == 'EV stock') & (data['unit'] == 'Vehicles')]


df = df[['year', 'value']].dropna()


df['year'] = pd.to_numeric(df['year'], errors='coerce')
df['value'] = pd.to_numeric(df['value'], errors='coerce')
df = df.dropna()  

X = df[['year']]
y = df['value']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)


model = LinearRegression()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)


mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation Metrics:")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R-squared (R²): {r2:.2f}")


future_year = np.array([[2020]])  
future_prediction = model.predict(future_year)

print(f"\nPredicted EV stock for the year {future_year[0][0]}: {future_prediction[0]:.2f}")