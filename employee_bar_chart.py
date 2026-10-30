import pandas as pd
import numpy as np 

df =pd.read_csv("/storage/emulated/0/Download/employee project/05_employee_attrition.csv")
import matplotlib.pyplot as plt
c="b","black","y","r","g"
df["department"].value_counts().plot(kind="bar",color=c)
plt.title("Employees by Department")
plt.ylabel("Number of employees")
plt.tight_layout()
plt.savefig("/storage/emulated/0/Download/employees_bar.png")
plt.show()