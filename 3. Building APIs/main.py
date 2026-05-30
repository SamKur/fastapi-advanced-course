from fastapi import FastAPI, HTTPException
from models_val import Employee
from typing import List

employees_db: List[Employee] = []   # here using simple list, but you can integrate sql db

app = FastAPI()


# 1. Read all employees
@app.get('/employees', response_model=List[Employee])
def get_employees():                # this 'Get Employee' will be shown in swagger beside GET /employees, this func is called ROUTE HANDLER
    return employees_db


# 2. Read specific employee
@app.get('/employees/{emp_id}', response_model=Employee)
def get_employee(emp_id: int):
    for index, employee in enumerate(employees_db):
        if employee.id == emp_id:
            return employees_db[index]
    raise HTTPException(status_code=404, detail='Employee Not Found')  # this msgs/code will be shown on err


# 3. Add an employee
@app.post('/add_employee', response_model=Employee)
def add_employee(new_emp: Employee):
    for employee in employees_db:
        if employee.id == new_emp.id:
            raise HTTPException(status_code=400, detail='Employee already exists') # shown in response body (json)
    employees_db.append(new_emp)
    return new_emp      # after add, it will also be shown is response body (json) as {"message":"..."}


# 4. Update an employee - by id
@app.put('/update_employee/{emp_id}', response_model=Employee)
def update_employee(emp_id: int, updated_employee: Employee):
    for index, employee in enumerate(employees_db):
        if employee.id == emp_id:
            employees_db[index] = updated_employee
            return updated_employee
    raise HTTPException(status_code=404, detail='Employee Not Found')


# 5. Delete an employee
@app.delete('/delete_employee/{emp_id}')
def delete_employee(emp_id: int):
    for index, employee in enumerate(employees_db):
        if employee.id == emp_id:
            del employees_db[index]
            return {'message': 'Employee deleted successfully'}
    raise HTTPException(status_code=404, detail='Employee Not Found')

