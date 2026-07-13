import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('data.csv')

# Data cleaning 
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
df=df.drop_duplicates()

# Numeric column cleaning 
df["price"] = df["price"].astype(str).str.replace(",", "").astype(float)
df["area"] = df["area"].astype(str).str.replace(",", "").astype(int)
df["rate_per_sqft"] = df["rate_per_sqft"].astype(str).str.replace(",", "").astype(int)


# Categorical column cleaning
