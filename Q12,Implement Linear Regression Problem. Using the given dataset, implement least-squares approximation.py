import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

areas = np.array([750, 1000, 1250, 1500, 1750, 2000]).reshape(-1, 1) 
prices = np.array([100000, 150000, 200000, 250000, 300000, 350000])

model = LinearRegression()
model.fit(areas, prices)

predicted_price = model.predict([[1700]])
print("Predicted price for a house with an area of 1700 sq.ft:", predicted_price[0])

plt.scatter(areas, prices, color='blue', label='Data points')
plt.plot(areas, model.predict(areas), color='red', label='Regression line')
plt.title('Linear Regression: House Prices vs. Area')
plt.xlabel('Area (sq.ft)')
plt.ylabel('Price ($)')
plt.legend()
plt.grid(True)
plt.show()