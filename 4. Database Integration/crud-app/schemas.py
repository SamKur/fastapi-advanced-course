from pydantic import BaseModel, EmailStr
# from typing import Optional


class EmployeeBase(BaseModel): # SHARED for DRY # inherits pydantic base model for type valdiation
    name: str
    email: EmailStr


class EmployeeCreate(EmployeeBase): # creating emp
    pass


class EmployeeUpdate(EmployeeBase): # updating emp
    pass


class EmployeeOut(EmployeeBase): # Output for returning emp data 
    id: int     # it will also have id, because when we want to show the employee
    class Config:  # NB: inside, needed for sqlalchemy
        orm_mode = True