########################IMPORTING#############################IMPORTING################################
import pandas as pd


df = pd.read_csv("pandas_python/src/data.csv")
 

#print(df) wont print all of it... only first 5 lines and last 5 files, you can do it other way
#tho it would print an entire csv file, so be careful:
print(df.to_string)