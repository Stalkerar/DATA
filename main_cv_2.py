
import pandas as pd # dataframes
import numpy as np # matrices and linear algebra
import matplotlib.pyplot as plt # plotting
import seaborn as sns # another matplotlib interface - styled and easier to use


###########
#CV-2
###########
###############################
#We need to somehow mark the outliers in the data according to the SalePrice and GrLivArea
#One possibility is to compute IQR for both columns and mark outliers using lower and upper bounds
#Lower bound: Q1 - 1.5*IQR
#Upper bound: Q3 + 1.5*IQR
#If the house has SalePrice OR GrLivArea value outside of the bounds - it is an outlier
#Vizualize the data using scatter plot and distinguish the outlier and non-outlier data using different colors (hue)
################################
#df_full.SalePrice.describe()
#df_full.SalePrice.quantile(0.25)

df_full = pd.read_csv('datasets/zsu_cv1_data.csv', sep=',')

x = df_full['SalePrice'].quantile(0.25)
x2 = df_full['SalePrice'].quantile(0.75)
y1 = df_full['SalePrice'].quantile(0.25) - 1.5*(x2 - x)
y2 = df_full['SalePrice'].quantile(0.75) + 1.5*(x2 - x)

c = df_full['GrLivArea'].quantile(0.25)
c2 = df_full['GrLivArea'].quantile(0.75)
v1 = df_full['GrLivArea'].quantile(0.25) - 1.5*(c2 - c)
v2 = df_full['GrLivArea'].quantile(0.75) + 1.5*(c2 - c)

df_full['Outlier'] = False
df_full.loc[(((df_full['SalePrice'] < y1) | (df_full['SalePrice'] > y2))) | (((df_full['GrLivArea'] < v1) | (df_full['GrLivArea'] > v2))),'Outlier'] = True

fig = plt.figure(figsize=(16, 9))
sns.scatterplot(data=df_full,x='GrLivArea',y='SalePrice',hue=('Outlier','Sale'),alpha=1)
plt.show()


################
#Try to vizualize the relationship between SalePrice and OverallQual
#You can use BoxPlots, Scatter plots, etc.
#Describe the insight you got from the plots with a few sentences
#Do the same for SalePrice and OverallCond; i.e. vizualize and describe insight
#################

sns.boxplot(data=df_full,x='OverallQual',y='SalePrice')
plt.show()
#Z grafu je patrná přímá lineární úměra, kde můžeme prohlásit, že se zvyšující se kvalitou stoupá i cena.
sns.boxplot(data=df_full,x='OverallCond',y='SalePrice')
plt.show()
#Na grafu je zajímavé, že nejčastější celkové hodnocení je střední hodnota, v níž se nachází objekty všech cenových hladin,
#tudíž můžeme prohlásit, že celkové hodnocení kvality se nepromítá na výšce ceny.