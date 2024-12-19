import pandas as pd
import sqlite3

data_csv = pd.read_csv('percent-bachelors-degrees-women-usa.csv')
#print(data_csv)

data_txt = pd.read_csv('StudentsSchools.txt',header = 0,sep = ',')
# print(data_txt)

# Read excel file 

# data_excel = pd.read_excel('file.xlsx',sheet_name='Hoja1')

data_json = pd.read_json('prices.json')
# print(data_json)

# SQL Connection

# connection_db = sqlite3.connect("database_name.db")
# query_1 = 'SELECT col_1 FROM table_name'
# query_2 = 'SELECT * FROM table_name'
# data_sql = pd.read_sql(query_1,connection_db)
# print(data_sql)