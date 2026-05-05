import pandas as pd

df = pd.read_csv("pandas_python/src/data.csv")

# #1. Drop irrelevant columns
#df = df.drop(columns=["Legendary","No"]) #removes 'Legendary' column and 'No'


# #2. Handle missing data
#df = df.dropna(subset=["Type2"]) #removes rows which don't have 'Type2'
#df = df.fillna({"Type2" : "None"}) #we are using dictionary here, so that if Type2 has no attribute it would be replaced by 'None'


# #3. Fix inconsistent values | literally replacing names, idk how to explain in other words
# df["Type1"] = df["Type1"].replace({"Grass": "GRASS",
#                                    "Fire" : "FIRE",
#                                    "Water" : "WATER"})


# 4. Standirdize text
df["Name"] = df["Name"].str.lower() #makes all of em lowercase


# 5. Fix data types
df["Legendary"] = df["Legendary"].astype(bool) #converts it fully to a boolean. cool shyt gng

# 6. Remove duplicate values
df = df.drop_duplicates()


print(df.to_string())