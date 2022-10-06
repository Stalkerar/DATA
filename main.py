
import pandas as pd # dataframes
import numpy as np # matrices and linear algebra
import matplotlib.pyplot as plt # plotting
import seaborn as sns # another matplotlib interface - styled and easier to use

#############
#Add a new column Undervalued which is set to True in case that the house is priced bellow 163k USD and has both OverallQual and OverallCond higher than 5.
#How many undervalued houses are in the dataset?
############# 4//,2,8,16,17,22

df_full = pd.read_csv('datasets/zsu_cv1_data.csv', sep=',')
df_full['Undervalued'] = False
df_full.loc[((df_full['OverallCond'] > 5) & (df_full['SalePrice'] < 163000) & (df_full['OverallQual'] > 5)),'Undervalued'] = True
print(df_full['Undervalued'].value_counts())

############
#Add to dataframe new attribute determining if the house was build before or after year 2000.
#create bar chart for number of houses depending on type of dwelling (attribute BldgType, use as a category axis) and
#added binary attribute about house age (use as a bar color).
############
df_full['New'] = False
df_full.loc[df_full['YearBuilt'] > 2000,'New'] = True
df_bld_new = df_full.groupby(['BldgType','New']).Id.count().reset_index(name='Count')
sns.barplot(data = df_bld_new, x='Count',y='BldgType',hue= 'New')
plt.show()



df_full[['SalePrice','GrLivArea']].head()
#df['YearQuartedSoldAplly'] = df.loc[:,['MoSold','YrSold']].apply(lambda x: f'{x[1]}-{x[0]//4+1}',axis=1)
#df.YearQuartedSoldAplly