import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('english.csv')

plt.figure(figsize=(16,4))
plt.barh(y=df['id'], width=df['speaking'])
plt.show()