from scipy.stats import pearsonr
import pandas as pd

data = pd.read_csv("Education_and_Consumption_Data.csv")

education_mapping = {'Basic': 1, '2n Cycle': 2, 'Graduation': 3, 'Master': 4, 'PhD': 5}
data['Education_Level'] = data['Education'].map(education_mapping)
consumption_columns = ['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']
data['Total_Consumption'] = data[consumption_columns].sum(axis=1)
data = data.dropna(subset=['Education_Level', 'Total_Consumption'])

# Pearson correlation
correlation, p_value = pearsonr(data['Education_Level'], data['Total_Consumption'])
print("Correlation:", correlation)
print("P-value:", p_value)
#(0.10760961929536286, 3.3078843266982846e-07)


from scipy.stats import t
n = len(data['Education_Level'])
# t-statistic
t_statistic = (correlation * (n - 2) ** 0.5) / ((1 - correlation ** 2) ** 0.5)
# p-value
p_value_t_test = 2 * t.sf(abs(t_statistic), df=n - 2)
print("t_statistic:", t_statistic)
print("p_value:", p_value_t_test)


from scipy.stats import f_oneway
groups = [data['Total_Consumption'][data['Education_Level'] == level] for level in data['Education_Level'].unique()]
# ANOVA F-test
f_stat, p_value = f_oneway(*groups)
print("F-statistic:", f_stat)
print("P-value:", p_value)

#we reject the null hypothesis 𝐻0 for such small p-value, indicating a statistically significant correlation between education level and total consumption

import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(10, 6))
sns.regplot(x='Education_Level', y='Total_Consumption', data=data, ci=None)
plt.xlabel('Education Level')
plt.ylabel('Total Consumption')
plt.title('Correlation between Education Level and Total Consumption')
#plt.show()