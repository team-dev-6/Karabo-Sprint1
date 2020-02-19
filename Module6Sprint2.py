import numpy as np 
import matplotlib.pyplot as plt

import pandas as pd

data = pd.read_csv('data.csv')
data.plot(x='Cost', y='Profit', kind='scatter')

plt.show()
# Method 1

plt.scatter(x='Price', y='Cost', data=data)

plt.show()

# Method 2

plt.scatter(x=data['VAT returned'], y=data['AdjClose'])

plt.show()
