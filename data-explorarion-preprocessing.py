import pandas as pd

data_csv = pd.read_csv('percent-bachelors-degrees-women-usa.csv')

# print(data_csv.head(20))
# print(data_csv.tail(5))
# print(data_csv.info())

# Drop missing values

data_csv.dropna()

# Fill missing values

data_csv.fillna("NULL")

# Delete duplicates

data_csv.drop_duplicates()

# Get row by integer index
print(data_csv.iloc[10])

data = pd.DataFrame({
    'A1': [1,2,3],
    'A2': [4,5,6],
    'A3': [7,8,9],
},index=['X','Y','Z'])

print(data)
print(data.loc['X'])
print(data.loc[:,'A2'])
print(data.loc['Y','A2'])