
employees = [
    {"id": 1001, "salary": 65000},
    {"id": 1002, "salary": 100000},
    {"id": 1003, "salary": 35000},
    {"id": 1004, "salary": 55000},
    {"id": 1005, "salary": 25000},
    {"id": 1006, "salary": 95000},
]

sorted_by_salary = sorted(employees, key=lambda employee: employee["salary"])

for employee in sorted_by_salary:
    print(f"ID: {employee['id']} | Salary: {employee['salary']}")
