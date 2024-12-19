import pandas as pd
import numpy as np
from scipy import stats

data = [100,20,5,20,45,-100,46]

mean = np.mean(data)
median = np.median(data)
mode = stats.mode(data)
variance = np.var(data)
std = np.std(data)

# Descriptive statistics

data_csv = pd.read_csv('percent-bachelors-degrees-women-usa.csv')
print(data_csv.describe())