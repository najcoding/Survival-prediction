import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('Titanic Dataset (3).csv')
data.head(5)
data.dtypes
nominal_cat = ['Name', 'Ticket', 'Cabin']
original_cat = ['Embarked', 'Gender']
data['Gender'].value_counts()
gender_categories = ['Females', 'Males']
data['Gender'] = pd.Categorical(data['Gender'], gender_categories, ordered = True)
median_index = np.median(data['Gender'].cat.codes)
median_gender = gender_categories[int(median_index)]
print(median_gender)
data['Embarked'].value_counts()
embarked_categories = ['s', 'c', 'g']
data['Embarked'] = pd.Categorical(data['Embarked'], embarked_categories, ordered = True)
median_Index = np.median(data['Embarked'].cat.codes)
median_embarked = embarked_categories[int(median_index)]
print(median_embarked)