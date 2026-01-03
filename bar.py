import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('csv/ielts.csv')
values=[
    df.writing.mean(),
    df.speaking.mean(),
    df.reading.mean(),

]
labels=['reading','speaking','writing']
plt.figure(figsize=(16,8))
plt.plot(values)
plt.show()


















# df=pd.read_csv('ielts.csv')

# plt.figure(figsize=(16,9))
# sns.barplot(data=df.sample(50),x='reading',y='writing')
# plt.show()