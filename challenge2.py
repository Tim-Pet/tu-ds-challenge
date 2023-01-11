import os
import pandas as pd

# --------------
# Import the Data
# --------------
# Get the current working directory
print(os.getcwd())
df = pd.read_csv('final_dataset.csv', sep=',')

# Therefore, it is important to get familiar with the data.
# Note: In case of problem please feel free to contact your peers or your mentor.
# CO2 Vehicle Emission Dataset
# The logical step is to import the dataset in order to get a better understanding of the dataset. Therefore, you can use your knowledge of the lesson “Data Structure”, especially DataFrames. Maybe the following lines could be a starting point for you.

# Code skeleton
# @author: Dr. Benjamin M. Abdel-Karim
# @since: 2022-07-22
import os
import pandas as pd

# --------------
# Import the data
# --------------
# Get the current working directory
print(os.getcwd())

df = pd.read_csv('../data/final_dataset.csv', sep=',')
print(df.info())

# Let's see what attributes/columns we have.
print(df.columns)

# There are quite some columns. How many, actually?
print(len(df.columns))