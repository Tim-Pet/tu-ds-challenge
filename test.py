# Code skeleton
# @author: Dr. Benjamin M. Abdel-Karim
# @since: 2022-10-02

# Imports
import os
import pandas as pd

# --------------
# Import the Data
# --------------
# Get the current working directory
print(os.getcwd())

df = pd.read_csv('data.csv', sep=',')
print(df.info())

# Let's see what attributes/columns we have.
print(df.columns)

# There are quite some columns. How many, actually?
print(len(df.columns))

# ------------------------------------------
# Pre-Processing
# ------------------------------------------
# Data pre-processing
# Let's check the data set for missing values.
# @code: 0, or â€˜indexâ€™: Drop rows which contain missing values.
# Let's see where the Null values are.
# Let's see the data shape and NaN values.
# This will give number of NaN values in every column.
df_null_values = df.isnull().sum()
print('NANs?', df_null_values)

# Show missing values in a figure
# plt.figure(figsize=(15,5))
# sns.heatmap(df.isnull(), cbar=False, yticklabels=False, cmap='Greys')
# plt.xticks(rotation=45, fontsize=6)
# plt.tight_layout()
# plt.savefig('fig_MissingValues.pdf')
# plt.close()

# Drop all rows with NaN.
df = df.dropna(axis=0)
df_null_values = df.isnull().sum()
print('NANs_After_Update?', df_null_values)
print('// complete ........ Pre-Processig')

# ... 

df['LÃ¤ngengrad'] = df['LÃ¤ngengrad'].astype(float)

# ... 

# Select the feature set. 
list_columns = ['Anschlussleistung', 'Anzahl Ladepunkte', 'dummy_super_charger']
X = df[list_columns].to_numpy()

...

# ------------------------------------------
# Modeling the Data
# ------------------------------------------
# @sorce: https://towardsdatascience.com/k-means-clustering-with-scikit-learn-6b47a369a83c
from sklearn.cluster import KMeans


