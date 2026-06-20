from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


all_customer = [{"id": 101, "name": "ram", "city":"Mumbai", "risk":"high"},
                {"id": 102, "name": "aditya", "city":"Delhi", "risk":"high"},
                {"id": 103, "name": "satyam", "city":"Mumbai", "risk":"medium"},
                {"id": 104, "name": "omprakash", "city":"Mumbai", "risk":"low"},
                {"id": 105, "name": "jayesh", "city":"Mumbai", "risk":"high"},
                
                ]

@app.get("/customers/")
def get_customers(city:str, risk: str):
    filter = [
                c for c in all_customer
                if c["city"] == city and c["risk"] == risk
              ]


    return {
        "city": city,
        "risk": risk,
        "count": len(filter),
        "result": filter
    }
