import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('ielts.csv')

plt.figure(figsize=(16,9))
sns.barplot(data=df.sample(50),x='reading',y='writing')
plt.show()