#libraries for machine learning
#1.sckit-learn
#2.pandas
#3. numpy
#4.matplotlib
#5.tensorFlow and PyTorch

#builing your first model
#example: predicting housing prices
#1.data preparation
from sklearn.datasets import load_boston
import pandas as pd
# Load dataset
boston = load_boston()
df = pd.DataFrame(boston.data, columns=boston.feature_names)
df['MEDV'] = boston.target
#2.data spitting
from sklearn.model_selection import train_test_split
X = df.drop('MEDV', axis=1)
y = df['MEDV']
X_train, X_test, y_train, y_test = train_test_split(X, y,
test_size=0.2, random_state=42)
#3.model training
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
#4.making predictions and evaluating the model
from sklearn.metrics import mean_squared_error
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)
#5.visualization
import matplotlib.pyplot as plt
plt.scatter(y_test, y_pred)
plt.xlabel("Prices: $Y_i$")
plt.ylabel("Predicted prices: $\hat{Y}_i$")
plt.title("Prices vs Predicted prices: $Y_i$ vs $\hat{Y}_i$")
plt.show()