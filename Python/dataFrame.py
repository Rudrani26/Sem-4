import pandas as pd

# df = pd.DataFrame({'X': [1, 2, 3, 4, 5], 'Y': [
#                   6, 7, 8, 9, 10], 'Z': [11, 23, 34, 45, 56]})
# print(df)

import numpy as np

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Rudrani', 'Upadnya', 'Yojak'],
             'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
             'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels)
print(df)
print("================================================")
print(df.iloc[:3])
print("================================================")
print(df[df['attempts'] > 2])
print("================================================")
print(df[df['score'].between(15, 20)])
print("================================================")
print(df['score'].mean())
print("================================================")
df.loc['k'] = ['Aarti', 34, 3, 'no']
print(df)
df = df.drop('k')
print(df)
print("================================================")
color = ['Red', 'Blue', 'Orange', 'Red', 'White',
         'White', 'Blue', 'Green', 'Green', 'Red']
df['color'] = color
print(df)
print("================================================")
df.at[8, 'score'] = 10.2
print(df)
print("================================================")
print(df.loc[df['score'] == 20])
print("================================================")
print(df.iloc[0])
print("================================================")
print(df.add_prefix("*"))
print(df.add_suffix("$"))
print("================================================")
print(df.interpolate())
print("================================================")
