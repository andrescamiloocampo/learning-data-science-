import matplotlib.pyplot as plt
import numpy as np 
from scipy.stats import norm

x_values = [1,2,3,4,5,6,7,8,9,10]
y_values = [1,4,6,8,10,12,14,16,18,20]

# plt.plot(x_values, y_values,color='green')
# plt.xlabel('x-axis placeholder')
# plt.ylabel('y-axis placeholder')
# plt.title('Title placeholder'

# plt.scatter(x_values, y_values, color='red')
# plt.xlabel('x-axis placeholder')
# plt.ylabel('y-axis placeholder')
# plt.title('Title placeholder')
# plt.show()

# cat = ['cat','dog','horse','mouse']
# cat_value = [10,30,100,1]

# plt.bar(cat,cat_value,color='forestgreen')
# plt.xlabel('Animals')
# plt.ylabel('Weights')
# plt.title('Animal Weights')
# plt.show()

# X_normal = np.random.normal(0,1,100)
# plt.hist(X_normal,color="forestgreen")
# plt.xlabel('X')    
# plt.ylabel('Frequency')
# plt.title('Randomly Sampled Data from Standard Normal Distribution')
# plt.show()    


# Population distribution
X_normal = np.random.normal(0,1,100)
x_values = np.arange(-5,5,0.01)
y_values = norm.pdf(x_values)


counts, bins, ignored = plt.hist(X_normal,30,density=True,color='purple',label='Sampling Distribution') 
plt.plot(x_values,y_values,color='y',linewidth=2.5,label='Population Distribution')
plt.title('Randomly generated 1000 obs from Normal distribution mu = 0 sigma = 1')
plt.ylabel('Probability')
plt.legend()
plt.show()