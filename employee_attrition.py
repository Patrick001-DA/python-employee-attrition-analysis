import pandas as pd
import numpy as np

df=pd.read_csv("05_employee_attrition.csv")
#inspect dataset
print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
#Count employees and inspect missing values.
employees_count=len(df)
print(employees_count)
missing_values=df.isna().sum()
print(missing_values)#no missing values

#Calculate overall attrition rate as a percentage.
attrition_rate_pct=(df["attrition"].mean()* 100
print(attrition_rate_pct)
#Which department has the highest attrition rate?
print(df.groupby("department")["attrition"].mean().mul(100).sort_values(ascending=False))
#Compare attrition rates for employees with and without overtime.
without=df[df["overtime"]== "False"]
print(without)
with_overtime=df[df["overtime"]!="False"]
print(with_overtime)
#Calculate average monthly income by department
df=df.groupby("department")["monthly_income_kes_thousands"].mean()
print(df)
#Create a bar chart of employee count by department.
import matplotlib.pyplot as plt
df["department"].value_counts().plot(kind="bar")
plt.title("Employees by Department"); plt.ylabel("Number of employees")
plt.tight_layout(); plt.show()

#Describe one limitation of this small dataset.