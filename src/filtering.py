import pandas as pd

df = pd.read_csv("pandas_python/src/data.csv")


#Filtering = keeping the rows that match a condition
#sort of a WHERE from SQL in python pandas

tall_pokemon = df[df["Height"] >= 2] #filters by height
heavy_pokemon = df[df["Weight"] > 100] #filters by weight  
legendary_pokemon = df[df["Legendary"] == True] #filters by if it is legendary or not(boolean)
water_pokemon = df[(df["Type1"] == "Water") | #filters by 'class' or abilities I'd say
                   (df["Type2"] == "Water")]

ff_pokemon = df[(df["Type1"] == "Fire") & #here as well, it filters by abilities for fire and if it can fly or not
                (df["Type2"] == "Flying")]

print(ff_pokemon)