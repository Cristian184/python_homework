import csv
import os
from datetime import datetime
import custom_module

# Task 2
def read_employees():
    try:
        data = {}
        rows = []
        with open("../csv/employees.csv", "r") as f:
            reader = csv.reader(f)
            for idx, row in enumerate(reader):
                if idx == 0:
                    data["fields"] = row
                else:
                    rows.append(row)
        data["rows"] = rows
        return data
    except Exception as e:
     trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = list()
    for trace in trace_back:
      stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
    print(f"Exception type: {type(e).__name__}")
    message = str(e)
    if message:
      print(f"Exception message: {message}")
    print(f"Stack trace: {stack_trace}")

employees = read_employees()
print(employees)

# Task 3: 
def column_index(col):
    return employees["fields"].index(col)

employee_id_column = column_index("employee_id")

# Task 4: 
def first_name(row_num):
    return employees["rows"][row_num][column_index("first_name")]

# Task 5: 

def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches = list(filter(employee_match, employees["rows"]))
    return matches

# Task 6: 
def employee_find_2(employee_id):
    return list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))

# Task 7: 
def sort_by_last_name():
    employees["rows"].sort(key=lambda row: row[column_index("last_name")])
    return employees["rows"]

print(sort_by_last_name())

# Task 8: 
def employee_dict(row):
    return {k: v for k, v in zip(employees["fields"], row) if k != "employee_id"}

print(employee_dict(employees["rows"][0]))

# Task 9: 
def all_employees_dict():
    return {
        row[employee_id_column]: employee_dict(row)
        for row in employees["rows"]
    }

print(all_employees_dict())

# Task 10: 
def get_this_value():
    return os.getenv("THISVALUE")

# Task 11: 

def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("Sanctuary")
print(custom_module.secret)

# Task 12: 
def read_csv_to_dict(filepath):
    with open(filepath, "r") as f:
        reader = csv.reader(f)
        fields = next(reader)
        rows = [tuple(row) for row in reader]
    return {"fields": fields, "rows": rows}

def read_minutes():
    return read_csv_to_dict("../csv/minutes1.csv"), read_csv_to_dict("../csv/minutes2.csv")

minutes1, minutes2 = read_minutes()
print(minutes1)
print(minutes2)

# Task 13: 
def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    return set1.union(set2)

minutes_set = create_minutes_set()
print(minutes_set)

# Task 14: 
def create_minutes_list():
    minutes = list(minutes_set)
    return list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes))

minutes_list = create_minutes_list()
print(minutes_list)

# Task 15: 
def write_sorted_list():
    minutes_list.sort(key=lambda x: x[1])
    converted = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), minutes_list))
    with open("minutes.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(minutes1["fields"])
        writer.writerows(converted)
    return converted

print(write_sorted_list())