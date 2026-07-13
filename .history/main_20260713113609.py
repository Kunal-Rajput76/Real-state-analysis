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
df["status"] = df["status"].str.strip().str.lower()
df["rera_approval"] = df["rera_approval"].str.strip().str.lower().map({"approved by rera": True, "not approved by rera": False})
df["flat_type"]=df["flat_type"].str.strip().str.lower()
df=df.drop_duplicates()

#question 1: Which is the costliest flat in the dataset?
costliest_flat=df.loc[df['price'].idxmax()]
# print(f"The costliest flat in the dataset is a {costliest_flat['property_type']} located in {costliest_flat['locality']}. It has an area of {costliest_flat['area']} sqft, priced at {costliest_flat['price']/10000000} crores in {costliest_flat['company_name']}, with a rate per sqft of {costliest_flat['rate_per_sqft']}. The flat is currently {costliest_flat['status']} and has RERA approval status: {costliest_flat['rera_approval']}. It is part of the society {costliest_flat['society']} and built by {costliest_flat['builder_name']}.")

# question 2: which locality has the highest average price ?
locality_avg_prices = df.groupby('locality')['price'].mean()
highest_locality = locality_avg_prices.idxmax()
# print(highest_locality)

# Question 3: which locality has the highest rate per sqft?
highest_rate_locatlity = df.groupby('locality')['rate_per_sqft'].mean().idxmax()
# print(f" The locatlity with the highest rate per square foot is {highest_rate_locatlity}.")

# question 4: Do ready-to-move properties cost more than under-construction properties ?
ready_to_move_avg_price = df[df['status'] == 'ready to move']['price'].mean()
under_construction_avg_price = df[df['status'] == 'under construction']['price'].mean()
# if ready_to_move_avg_price > under_construction_avg_price:
#     print("Ready-to-move properties cost more than under-construction properties.")     
# else:
#     print("Under-construction properties cost more than ready-to-move properties.")

# question 5: Do RERA-approved properties command a price premium ?
rera_approved_avg_price = df[df['rera_approval'] == True]['price'].mean()
rera_not_approved_avg_price = df[df['rera_approval'] == False]['price'].mean()
# if rera_approved_avg_price > rera_not_approved_avg_price:     
#     print("RERA-approved properties command a price premium.")