import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


df = pd.read_csv("/Users/maksudaydinisik/PycharmProjects/Machine_learning_notes/datasets/advertising.csv")
df = sns.load_dataset("tips")
print(df.head())

df["sex"].value_counts()
sns.countplot(x=df["sex"], data=df)     # countplot sütun grafiği oluşturur.
plt.show()

## Matplotlib
df['sex'].value_counts().plot(kind='bar')
plt.show()

# Sayısal Değişken Görselleştirme
sns.boxplot(x=df["total_bill"]) # kutu grafiği oluşturur.
plt.show()

df["total_bill"].hist() # histogram oluşturur.
plt.show()