import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('csv/english.csv')
values = [[df['listening'].mean(),
          df['reading'].mean(),
          df['writing'].mean(),
          df['speaking'].mean()]]

labels = ['listening', 'reading', 'writing', 'speaking']
plt.table(cellText=values,colLabels=labels)
plt.savefig('pictures/my.svg')
plt.tight_layout()
plt.show()
