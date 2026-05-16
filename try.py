import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

np.random.seed(42)

ad_spend = np.random.uniform(1000, 10000, 200)
store_traffic = ad_spend * np.random.uniform(0.5, 1.5, 200) + np.random.normal(0, 500, 200)
sales = (ad_spend * 2.5) + (store_traffic * 1.2) + np.random.normal(5000, 2000, 200)
competitor_price = np.random.uniform(10, 50, 200) 

df = pd.DataFrame({
    'Ad_Spend': ad_spend,
    'Store_Traffic': store_traffic,
    'Competitor_Price': competitor_price,
    'Total_Sales': sales
})
corr_matrix = df.corr()
print(corr_matrix)

X = df[['Ad_Spend', 'Store_Traffic']] # Features (inputs)
y = df['Total_Sales']                 # Target (output)

plt.scatter(df['Ad_Spend'],df['Total_Sales'])
plt.xlabel("Ad Spend")
plt.ylabel("Total Sales")
plt.title("Ad Spend vs Total Sales")
plt.show()

plt.scatter(df['Store_Traffic'],df['Total_Sales'])
plt.xlabel("Store Traffic")
plt.ylabel("Total Sales")
plt.title("Store Traffic vs Total Sales")
plt.show()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("\n--- Model Evaluation ---")
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"R-squared (R2): {r2:.2f}")

print("\n--- Model Coefficients ---")
print(f"Intercept (Base Sales): {model.intercept_:.2f}")
print(f"Ad Spend Multiplier: {model.coef_[0]:.2f}")
print(f"Store Traffic Multiplier: {model.coef_[1]:.2f}")