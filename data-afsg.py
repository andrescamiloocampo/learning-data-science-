import pandas as pd

# Create dataframe with sample data
data = pd.DataFrame({'Name':["Anna","Karen","John","Alice","Kevin","Sanna","Bob","Emily"],
                     'Age': [35,30,57,65,25,19,20,65],
                     'Salary': [20000, 60000, 145000, 170000,30000, 10000,220000, 120000],
                     'Department': ["Tech","Tech","Tech","Healthcare","Operations","Operations","Tech","Tech"]
                     })

# Sorting data

# Ascending order by default is true
data.sort_values(by = "Salary")

# Descending order
data.sort_values(by = "Salary", ascending = False)

# Grouping data

employees_per_department = data.groupby("Department")["Name"].count()
salary_per_department = data.groupby("Department")["Salary"].mean()
minimum_per_department = data.groupby("Department")["Salary"].min()
maximum_per_department = data.groupby("Department")["Salary"].max()
avg_ages_per_department = data.groupby("Department")["Age"].mean()


# Filtering data

print(data[data["Salary"] > 20000])

print("\n",data[(data["Salary"] > 20000) & (data["Salary"] < 200000)])

print("\n",data[data["Age"].isin([20,65])])