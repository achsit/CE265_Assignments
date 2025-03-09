#Import libraries
import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv('Data for model.csv')

# # Inspect the data
# print(data.head())
# print(data.info())
# print(data.describe())

# # Compute descriptive statistics for all variables
# descriptive_stats = data.describe().T[['mean', 'std']]
# print(descriptive_stats)

# Compute correlation matrix
correlation_matrix = data.corr()

# Plot heatmap of correlations
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, cmap='coolwarm', annot=False)
plt.title('Correlation Matrix')
plt.show()
