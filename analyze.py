import pandas as pd
import numpy as np


df = pd.read_csv('diabetes.csv')
# print(df.head())
# print(df.info(), df.describe())
# df.describe()

X = df.drop(columns=['Outcome'], axis=1)
y = df['Outcome']

Na = df.isna().sum()
print(Na)