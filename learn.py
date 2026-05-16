import pandas as pd 
import os
csv_path = os.path.join(os.path.dirname(__file__),'student_marks.csv')
df=pd.read_csv(csv_path)
# print(df)
# print(df.head())
# print(df.tail(3))
# # print(df.shape())
# print(df.info())
# print(df.describe())
# print(df.columns)
# names_series=df['Name']
# print(names_series)
# print(type(names_series))
# print(type(df))
# print(df.iloc[0])
# print(df.loc[0,'Name'])
# print(df.iloc[0:3, 1:3])
january_sales = pd.DataFrame({"Item":["Apple", "Banana"], "sales":[100, 150]})
february_sales = pd.DataFrame({"Item":["Cherry", "Dates"], "sales":[200, 50]})
master_sales = pd.concat([january_sales,february_sales], ignore_index=True)
print("Master Sales Table (Concatenated):\n",master_sales)
employees = pd.DataFrame({
    "Emp_ID": [1,2,3],
    "Name": ["John", "Sarah", "Mike"]
})
salaries = pd.DataFrame({
    "Emp_ID": [1,2,3],
    "Name": ["60000", "80000", "75000"]
})
full_employees_data = pd.merge(employees,salaries, on="Emp_ID")
print("Merged Employees Table:\n",full_employees_data)
                          