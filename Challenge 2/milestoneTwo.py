# --------------
# Import the Data
# --------------
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import locale
from locale import atof

# Get the current working directory & define tha data path
print(os.getcwd())
path = str(os.getcwd())+'/data/data.csv'

# Define the data frame
df = pd.read_csv(path, sep=';', encoding='ISO-8859-1', header=10, skipinitialspace=True)
print(df.info())

# --------------
# Milestone 2 - Basic Data infos
# --------------
# Log the shape (rows, columns) of the df [would work with: print(len(df.columns)) as well]
print(df.shape)

# Log the column types
print(df.dtypes)


# --------------
# Milestone 3 - Data Preprocessing
# --------------

# --------------
# 3.1 Add proper types
# --------------

# Set locale to work with german commas as decimal seperator to convert strings to float
locale.setlocale(locale.LC_NUMERIC, '')

# Declare final dtypes we want to have
df_dtypes = {
    "Betreiber"                 : "string",
    "Straße"                    : "string",
    "Hausnummer"                : "string", # String, since we have stuff like 10c as well here
    "Adresszusatz"              : "string",
    "Postleitzahl"              : "uint32",
    "Ort"                       : "string",
    "Bundesland"                : "string",
    "Kreis/kreisfreie Stadt"    : "string",
    "Breitengrad"               : "float32", 
    "Längengrad"                : "float32", 
    "Inbetriebnahmedatum"       : "datetime64",
    "Anschlussleistung"         : "float32", 
    "Normalladeeinrichtung"     : "object", # Should be boolean?
    "Anzahl Ladepunkte"         : "uint32",
    "Steckertypen1"             : "string", # enum?
    "P1 [kW]"                   : "float32", 
    "Public Key1"               : "string", 
    "Steckertypen2"             : "string",
    "P2 [kW]"                   : "float32", 
    "Public Key2"               : "string", 
    "Steckertypen3"             : "string",
    "P3 [kW]"                   : "float32", 
    "Public Key3"               : "string", 
    "Steckertypen4"             : "string",
    "P4 [kW]"                   : "float32", 
    "Public Key4"               : "string", 
}



def clean_dtypes(df, column_name, final_dtype):
    try:
        if final_dtype == "object":
            return df[column_name].astype(final_dtype)
        elif final_dtype == "uint32" or final_dtype == "uint64":
            return df[column_name].replace(np.nan, 0).astype(final_dtype)
        elif final_dtype == "float32" or final_dtype == "float64":
            return df[column_name].astype(str).apply(atof).astype(final_dtype)
        elif final_dtype == "string":
            return df[column_name].astype(final_dtype)
        elif final_dtype == "datetime64":
            return pd.to_datetime(df[column_name], format="%d.%m.%Y")
        return df[column_name].astype(final_dtype) # return the passed dtype without modification as a fallback
    except Exception as e:
        print("Error while converting column: " + column_name + " to dtype: " + final_dtype)
        print(e)
        return df[column_name]
    

def convert_dtypes(df, dtypes):
    for column, dtype in dtypes.items():
        df[column] = clean_dtypes(df, column, dtype)
    return df

converted_df = convert_dtypes(df, df_dtypes)
print(converted_df.dtypes)


# --------------
# Milestone 3.1 - draw table which visualises the missing values
# --------------

df_null_values = df.isnull().sum()
print('NANs?', df_null_values)

plt.figure(figsize=(15,5))
sns.heatmap(df.isnull(), cbar=False, yticklabels=False, cmap='Greys')
plt.xticks(rotation=45, fontsize=6)
plt.tight_layout()
plt.savefig('pyplots/milestone_three_missing_values.pdf')
plt.close()


# --------------
# Milestone 3.2 - draw table which visualises the missing values
# --------------

# --------------
# Milestone 3.3 - clean outliers
# --------------


# --------------
# Milestone 3 - draw table which visualises the missing values
# --------------

# Drop all rows with NaN.
df = df.dropna(axis=0)
df_null_values = df.isnull().sum()
print('NANs_After_Update?', df_null_values)
print('// complete ........ Pre-Processing')