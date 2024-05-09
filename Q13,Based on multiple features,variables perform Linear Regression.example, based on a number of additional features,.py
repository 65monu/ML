import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Sample dataset of house prices and features
features = np.array([[3, 0, 2, 5], [4, 1, 1, 7], [2, 0, 3, 3], [5, 1, 2, 10], [4, 0, 2, 8], [3, 0, 1, 4]]).reshape(-1, 4)
prices = np.array([250000, 300000, 200000, 350000, 320000, 230000])

model = LinearRegression()
model.fit(features, prices)

sample_house = np.array([4, 1, 2, 6]).reshape(1, -1)

predicted_price = model.predict(sample_house)
print("Predicted price for the sample house:", predicted_price[0])

print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)