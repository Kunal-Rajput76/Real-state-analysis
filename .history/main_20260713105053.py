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
'''
 price                                1226300000.0
status                              ready to move
area                                        16500
rate_per_sqft                               74323
property_type    6 BHK Apartment in DLF Camellias
locality                                Sector 42
builder_name                    Provident Capital
rera_approval                               False
bhk_count                                       6
society                             DLF Camellias
company_name                                  DLF
flat_type                               apartment
'''
print(costliest_flat)