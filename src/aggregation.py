import pandas as pd

#aggregate functions = Reduces a set of values into a single summary line
#used to summarize and analyze data 
#Often used with groupby() function

df = pd.read_csv("pandas_python/src/data.csv")


# #they'd apply to the whole dataframe
# print(df.mean(numeric_only=True)) #mean number for all numeric columns
# print(df.sum(numeric_only=True)) #sum of all numeric columns
# print(df.min(numeric_only=True)) #min it speaks for itself
# print(df.max(numeric_only=True)) #max same shyt
# print(df.count()) #counts amount in each column



# #they'd to a single column
# print(df["Height"].mean()) #mean
# print(df["Height"].sum()) #sum 
# print(df["Height"].min()) #min 
# print(df["Height"].max()) #max 
# print(df["Height"].count()) #counts 


#the following code is going to group by everything with Type1 and we need another column to pass
#so it won't be alone by itself. So here, the first column is showing its type and the second one mean of their heights
#e.g for bug, for dragon, for electric ones etcetera 
group = df.groupby("Type1")

print(group["Height"].mean())
print(group["Height"].sum())
print(group["Height"].min())
print(group["Height"].max())
print(group["Height"].count())