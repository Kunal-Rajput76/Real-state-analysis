import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('data.csv')

# Data cleaning 
df.columns=df.columns.str.strip().str.lower().str