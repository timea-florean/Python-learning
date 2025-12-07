#Pandas
#pip install pandas
#basic operations
import pandas as pd
#creating a DataFrame
data={'Name':['John','Anna','James'],'Age':[28,22,35]}
df=pd.DataFrame(data)
#display the DataFrame
print(df)

#basic data manipulation
#selecting data

#selecting a column
print(df['Name'])

#selecting multiple columns
print(df[['Name','Age']])

#selecting rows by position
print(df.iloc[1])

#selecting rows by condition
print(df[df['Age']>25])

#Adding a new column
df['Employed'] = [True, True, False]
print(df)
# Removing a column
df.drop('Employed', axis=1, inplace=True)
print(df)

# Sorting by a column
df_sorted = df.sort_values(by='Age')
print(df_sorted)

#Grouping by a column and aggregating
df_grouped = df.groupby('Age').size()
print(df_grouped)

#Visualizing data

import matplotlib.pyplot as plt
# Plotting data directly from a DataFrame
df.plot(kind='bar', x='Name', y='Age')
plt.ylabel('Age')
plt.title('Bar Chart of Ages')
plt.show()

#we're going to use Seaborn for more complex visualizatios
import seaborn as sns
# Creating a histogram
sns.histplot(df['Age'], bins=10, kde=True)
plt.title('Distribution of Ages')
plt.show()
# Creating a boxplot
sns.boxplot(x='Age', data=df)
plt.title('Boxplot of Ages')
plt.show()