import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('csv/english.csv')

plt.figure(figsize=(10,4))
plt.barh(y=df['id'], width=df['speaking'])
plt.savefig('pictures/brath.svg')
plt.show()