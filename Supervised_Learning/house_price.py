import pandas as pd
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

boston = load_boston()
data = pd.DataFrame(boston.data, columns=boston.feature_names)
data['target'] = boston.target

X = data.drop('target', axis=1)
y = data['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print('Mean squared error:', mse)

new_data = pd.DataFrame({
    'CRIM': [0.1],
    'ZN': [20],
    'INDUS': [6.0],
    'CHAS': [0],
    'NOX': [0.5],
    'RM': [5],
    'AGE': [60],
    'DIS': [5],
    'RAD': [4],
    'TAX': [300],
    'PTRATIO': [15],
    'B': [350],
    'LSTAT': [10]
})
prediction = model.predict(new_data)
print('Predicted price:', prediction[0])
