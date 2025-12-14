import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df =pd.read_csv('csv/ielts.csv')
values=[
    df.reading.mean(),df.speaking.mean(),df.writing.mean()
]
labels=['reading','writing','speaking']
plt.figure(figsize=(16,10))
plt.pie(values,labels=labels,autopct='%1.1f%%',startangle=True)
plt.savefig('pictures/category.png')
plt.show()