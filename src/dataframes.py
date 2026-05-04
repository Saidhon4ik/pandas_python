###############DATAFRAMES#######################DATAFRAMES#######################################
import pandas as pd

data = {"Name": ["Spongebob","Patrick","Squidward"],
        "Age" : [30,35,50],
        }

#converting dictionary to a dataframe

df = pd.DataFrame(data,index=["Employee 1","Employee 2","Employee 3"])    #df for data_frame

# #df for a guy with a given label:
# print(df.loc["Employee1"])        


# #df with a index, like. you get it
# print(df.iloc[0]) 


#add a new column:
df["Job"] = ["Cook","N/A","Cashier"]


#add new rows
new_rows = pd.DataFrame([{"Name": "Sandy",
                         "Age" : 28,
                         "Job": "Engineer"},
                         {"Name": "Eugene",
                         "Age" : 60,
                         "Job": "Manager"}],
                         index=["Employee 4","Employee 5"])
df = pd.concat([df,new_rows])


#for all of em:
print(df) 