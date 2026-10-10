import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('Titanic Dataset (3).csv')
data.head(5)
num_data = data.drop(['Name', 'Ticket', 'Cabin', 'Embarked', 'Gender'],  axis = 1)
labels = ['PassengerId', 'Survived', 'Pclass', 'Age', 'sibsp', 'Parch', 'Fare']
for label in labels:
    plt.boxplot(num_data[label])
    plt.show()
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler
num_data = scaler.fit_transform(num_data)