########################SERIES##############################################SERIES######################

# from ast import arg

# import pandas as pd 


# #Series one single colum
# data = [100,102,104,200,202]

# series = pd.Series(data) #after data you can add 'index = ["a","b","c"]' to change starting indexes
# #in output left side adds index, starting from zero   
# # print(series) 


# # print(series.loc[1]) #outputs a value with label =  1


# # # series.loc[1] = 2 #you can change a value by label
# # print(series.iloc[1])




# print(series[series >= 200])



####with dictionary
import pandas as pd

calories = {"Day 1": 1750,
            "Day 2": 2100,
            "Day 3": 1700}

series = pd.Series(calories) #no need in .index. Key : value

series.loc["Day 3"] += 500

print(series.loc["Day 1"])
print(series.loc["Day 2"])
print(series.loc["Day 3"])


print(series[series<2200])