import pandas as pd
 
# list of strings
lst = ['Geeks', 'For', 'Geeks', 'is', 
            'portal', 'for', 'Geeks']
 
# Calling DataFrame constructor on list
df = pd.DataFrame(lst)
print(df)


csvdata=pd.read_csv("file.csv",index-col="name")
#single row loc
#df.loc
first=csvdata.loc["vedavyas"]

#==== iloc  - retrive row and column by position
df.iloc[3]


#using isnull() function
df.isnull()

