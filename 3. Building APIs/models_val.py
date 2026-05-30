from pydantic import BaseModel, Field, StrictInt # check pydantic course code/notes
from typing import Optional, Annotated


class Employee(BaseModel):
    id: int = Field(..., gt=0, title='Employee ID') # we can also use Annotated
    name: str = Field(..., min_length=3, max_length=30) # default value OR ... for required
    department: str = Field(..., min_length=3, max_length=30)
    age: Optional[StrictInt] = Field(default=None, ge=21)
    salary: Annotated[int | None, Field(ge=21)] = None  # v2 syntax gold standard