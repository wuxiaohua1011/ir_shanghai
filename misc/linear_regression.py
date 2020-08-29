import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv(Path('../data/Salary_Data.csv'))
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=1 / 3)

lr = LinearRegression()
lr.fit(x_train, y_train)
y_pred = lr.predict(x_test)

plt.scatter(x_train, y_train, color="red")
plt.plot(x_train, lr.predict(x_train), color="green")
plt.title("Salary vs Experience (Training set)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()
