import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('english.csv')
values = [df['listening'].mean(),
          df['reading'].mean(),
          df['writing'].mean(),
          df['speaking'].mean()]

labels = ['listening', 'reading', 'writing', 'speaking']
plt.figure(figsize=(12,12))
plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.savefig('my.svg')
plt.show()
