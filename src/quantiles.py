import pandas as pd

# 1. Define fixed income data for 12 people
data = {
    'person_id': list(range(1, 13)),
    'monthly_income': [1200, 1500, 1800, 2200, 2500, 2800, 3100, 3500, 4000, 4500, 5000, 6000]
}

income_df = pd.DataFrame(data)

# 2. Calculate quantiles
q1 = income_df['monthly_income'].quantile(0.25)  # 25% mark
q2 = income_df['monthly_income'].quantile(0.5)   # 50% mark (median)
q3 = income_df['monthly_income'].quantile(0.75)  # 75% mark

# 3. Classify each person into an income bracket
def classify_income(income):
    if income <= q1:
        return 'Low income'
    elif income <= q2:
        return 'Middle income'
    elif income <= q3:
        return 'Upper-middle income'
    else:
        return 'High income'

# 4. Apply classification to the DataFrame
income_df['income_group'] = income_df['monthly_income'].apply(classify_income)

# 5. Print the results
print(income_df)

# 6. Summary of group counts
print("\nIncome Group Distribution:")
print(income_df['income_group'].value_counts())

'''
    person_id  monthly_income         income_group
0           1            1200           Low income
1           2            1500           Low income
2           3            1800           Low income
3           4            2200        Middle income
4           5            2500        Middle income
5           6            2800        Middle income
6           7            3100  Upper-middle income
7           8            3500  Upper-middle income
8           9            4000  Upper-middle income
9          10            4500          High income
10         11            5000          High income
11         12            6000          High income

Income Group Distribution:
income_group
Low income             3
Middle income          3
Upper-middle income    3
High income            3
Name: count, dtype: int64
'''