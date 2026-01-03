import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('csv/ielts.csv')
# df.drop('id',axis=1,inplace=True)
plt.figure(figsize=(20,10))
sns.lineplot(data=df.sample(30),color='black')
plt.savefig('pictures/bar.svg')
plt.show()