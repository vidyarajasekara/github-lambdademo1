import pandas as pd
path=r"C:\rawdata\namecity.csv"
data=pd.read_csv(path)
df=pd.DataFrame(data)
# print(df)
# print(df.dtypes)
# print(df['age'].dtype)
# print(df.columns)
# df = pd.DataFrame(data, columns=['name', 'city'])
# print(df.columns)

list_row = ["Johnathan", "Swiss", "40", 85.2]
# insert row
df.loc[108] = list_row
print(df)
# insert column
# new_column_values = ['value1', 'value2', 'value3', 'value4', 'value5', 'value6', 'value7', 'value8']
# df['New_Column'] = new_column_values
# print(df)

desig=['backend dev','frontend dev','manual tester','automation tester','sql developer','api developer','dataengineer','mechanical engineer']
df['designation']=desig
print(df)


# Sort the DataFrame by the 'age' column
# df = df.sort_values(by=['age'])
# df = df.sort_values(by=['age','py-score'], ascending=[True,True])
# df['age'] = df['age'].astype(int)
# df = df.sort_values(by=['age'])
# df = df.sort_values(by=['age','py-score'])
# select * from datas  order by age,py-score
# print(df)

# filter_age = df['age'] >= 35
# print(df[filter_age])


