import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('csv/english.csv')
fig, ax = plt.subplots(2,2, figsize=(16, 8))
fig.suptitle('English')
sns.lineplot(data=df,x=df.name,y=df.listening,ax=ax[0,0],color='red').grid(which='both')
sns.barplot(data=df,x=df.name,y=df.reading,ax=ax[0,1],color='black').grid(which='both')
sns.histplot(data=df,x=df.name,y=df.writing,ax=ax[1,0],color='blue').grid(which='both')
sns.boxplot(data=df,x=df.name,y=df.speaking,ax=ax[1,1],color='yellow').grid(which='both')
plt.savefig('pictures/english.svg')
plt.savefig('pictures/english.png')
plt.show()

