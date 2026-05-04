#####################################SELECTION##################################SELECTION##########################################
import pandas as pd

df = pd.read_csv("data.csv",index_col="Name") #index_col is sort of primary key here from SQL but for those files, idk if you got it or not


# #SELECTION BY COLUMN
# print(df["Name"].to_string())
# print(df["Height"].to_string())
# print(df["Weight"].to_string())

# print(df[["Name","Height","Weight"]].to_string()) #select columns, not one



#SELECTION BY ROW/S
print(df.loc["Charizard":"Pikachu",["Height","Weight"]])

print(df.iloc[0:11,0:3]) #first for rows, second for columns ig


#==========================================================================#



###################task##########################
pokemon = input("Enter a Pokemon's name: ").capitalize()

try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} was not found")