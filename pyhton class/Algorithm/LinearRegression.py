import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

house = pd.read_csv("house_data.csv")
print("Data preview")
print(house.head())

x = house[['square_feet']]
y = house[['price']]
3
x_train, x_test, y_train, y_test = train_test_split(
    x,y, test_size=0.2, random_state=20
)

model = LinearRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

house_price = float(input("Enter your cost: "))

print("MSE:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

input_house = pd.DataFrame([[house_price]], columns=['square_feet'])
prediction = model.predict(input_house)[0][0]
prediction = round(prediction,2)

def get_area(price):
    if price >= 400000:
        return "High price"
    elif price >= 350000:
        return "Medium price"
    elif price >= 250000:
        return "Normal price"
    elif price >= 150000:
        return "Low price"
    else:
        return "Lowest price"
        

print("Predicted Price:",prediction)
print("predicted Area:",get_area(prediction))