from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class application_p(BaseModel):
    name: str
    age : int
    income : float
    loan_ammount: float
    employeements_year: int

@app.post("/loan")
def loan_check_requiredment(application : application_p):

    approve = (application.income >=50000 and application.age >= 21 and application.employeements_year>=5)

    return { "name" : application.name,
            "loan_ammount": application.loan_ammount,
            "income": application.income,
            "Decision": "approve" if approve else "rejected",
            "reviewe_income":application.income
            }