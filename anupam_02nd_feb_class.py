# -*- coding: utf-8 -*-
"""Anupam 02nd Feb class.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1is3Evo-VVhd8c-QSCqC8HTrCDxsTjIlE
"""

# Importing important libraries
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# Importing the data
beml_df = pd.read_csv('/content/BEML.csv')
beml_df.head()

# Importing the data
glaxo_df = pd.read_csv('/content/GLAXO.csv')
glaxo_df.head()

# Filtering the required columns
beml_df = beml_df[['Date', 'Close']]
glaxo_df = glaxo_df[['Date', 'Close']]

# Getting the data types
beml_df.dtypes

# Getting the data types
glaxo_df.dtypes

# Creating the index
beml_df = beml_df.set_index(pd.DatetimeIndex(beml_df['Date']))
beml_df.head()

# Creating the index
glaxo_df = glaxo_df.set_index(pd.DatetimeIndex(glaxo_df['Date']))
glaxo_df.head()

# Data Visualization
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(5, 3))
plt.plot(glaxo_df.index, glaxo_df['Close'])
plt.xlabel('Year')
plt.ylabel('Closing Price')
plt.title('Closing Price of Glaxo')
plt.show()

# Data Visualization
plt.figure(figsize=(5, 3))
plt.plot(beml_df.index, beml_df['Close'])
plt.xlabel('Year')
plt.ylabel('Closing Price')
plt.title('Closing Price of BEML')
plt.show()

# Adding a 'gain' column
beml_df['gain'] = beml_df.Close.pct_change(periods = 1)
beml_df.head()

# Adding a 'gain' column
glaxo_df['gain'] = glaxo_df.Close.pct_change(periods = 1)
glaxo_df.head()

# Dropping the first row with NaN value
beml_df.dropna(inplace = True)
glaxo_df.dropna(inplace = True)

# Plot the gains
plt.figure(figsize = (5, 3))
plt.plot(beml_df.index, beml_df['gain'])
plt.xlabel('Year')
plt.ylabel('Gain')
plt.title('Gain of BEML')
plt.show()

# Plot the gains
plt.figure(figsize = (5, 3))
plt.plot(glaxo_df.index, glaxo_df['gain'])
plt.xlabel('Year')
plt.ylabel('Gain')
plt.title('Gain of Glaxo')
plt.show()

# Plot the gains
plt.figure(figsize = (5, 3))
plt.plot(beml_df.index, beml_df.gain, c= 'red')
plt.plot(glaxo_df.index, glaxo_df.gain, c= 'blue')
plt.xlabel('Year')
plt.ylabel('Gain')
plt.title('Gain of Glaxo and BEML')
plt.show()

# Density Plot for gain of Glaxo
import seaborn as sns
plt.figure(figsize = (5, 3))
sns.distplot(glaxo_df['gain'], label = 'Glaxo')
plt.xlabel('Gain')
plt.ylabel('Frequency')
plt.title('Density Plot for Gain of Glaxo')
plt.legend()
plt.show()

# Density Plot for gain of BEML
plt.figure(figsize = (5, 3))
sns.distplot(beml_df['gain'], label = 'BEML')
plt.xlabel('Gain')
plt.ylabel('Frequency')
plt.title('Density Plot for Gain of BEML')
plt.legend()
plt.show()

# Getting the Statistical properties
print('Mean :', round(glaxo_df['gain'].mean(), 4))
print('Standard Deviation :', round(glaxo_df['gain'].std(), 4))

# Getting the Statistical properties
print('Mean :', round(beml_df['gain'].mean(), 4))
print('Standard Deviation :', round(beml_df['gain'].std(), 4))

# Getting the 95% confidence interval
from scipy import stats
glaxo_df_ci = stats.norm.interval(0.95,
loc = glaxo_df.gain.mean(),
scale = glaxo_df.gain.std())

# Confidence Interval
print('Glaxo Confidence Interval :', np.round(glaxo_df_ci, 4))

# Question -> Finding the 95% confidence interval for beml_df
from scipy import stats
beml_df_ci = stats.norm.interval(0.95,
loc = beml_df.gain.mean(),
scale = beml_df.gain.std())

# Confidence Interval
print('BEML Confidence Interval :', np.round(beml_df_ci, 4))