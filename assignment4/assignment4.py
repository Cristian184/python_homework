# Task 1
import pandas as pd
import json
import numpy as np

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

task1_data_frame = pd.DataFrame(data)
print(task1_data_frame)

task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]
print(task1_with_salary)

task1_older = task1_with_salary.copy()
task1_older['Age'] += 1
print(task1_older)

task1_older.to_csv("employees.csv", index=False)


# Task 2
task2_employees = pd.read_csv("employees.csv")
print(task2_employees)

additional_employees = [
    {"Name": "Eve", "Age": 28, "City": "Miami", "Salary": 60000},
    {"Name": "Frank", "Age": 40, "City": "Seattle", "Salary": 95000}
]

with open("additional_employees.json", "w") as f:
    json.dump(additional_employees, f)

json_employees = pd.read_json("additional_employees.json")
print(json_employees)

more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print("\nTask 2 - Combined DataFrame:")
print(more_employees)

# Task 3
first_three = more_employees.head(3)
print("\nTask 3 - First Three Rows:")
print(first_three)

last_two = more_employees.tail(2)
print("\nTask 3 - Last Two Rows:")
print(last_two)

employee_shape = more_employees.shape
print("\nTask 3 - Shape of DataFrame:")
print(employee_shape)

print("\nTask 3 - DataFrame Info:")
more_employees.info()

# Task 4
# Load dirty_data.csv
dirty_data = pd.read_csv("dirty_data.csv")
print("\nTask 4 - Dirty Data:")
print(dirty_data)

# Create a copy
clean_data = dirty_data.copy()

clean_data = clean_data.drop_duplicates()
print("\nTask 4 - After Removing Duplicates:")
print(clean_data)

clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')
print("\nTask 4 - After Converting Age to Numeric:")
print(clean_data)

clean_data['Salary'] = clean_data['Salary'].replace(['unknown', 'n/a'], pd.NA)
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors='coerce')
print("\nTask 4 - After Cleaning Salary:")
print(clean_data)

clean_data['Age'] = clean_data['Age'].fillna(clean_data['Age'].mean())
clean_data['Salary'] = clean_data['Salary'].fillna(clean_data['Salary'].median())
print("\nTask 4 - After Filling Missing Values:")
print(clean_data)

clean_data["Hire Date"] = clean_data["Hire Date"].replace({
    "2020-03-18": "2020/03/18",
    "2019-07-11": "2019/07/22",
    "3/25/2019": "2019/03/25"
})
clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'], errors='coerce')
print("\nTask 4 - After Converting Hire Date:")
print(clean_data)

clean_data['Name'] = clean_data['Name'].str.strip().str.upper()
clean_data['Department'] = clean_data['Department'].str.strip().str.upper()
print("\nTask 4 - After Cleaning Text Fields:")
print(clean_data)
