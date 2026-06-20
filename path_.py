from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

customer_risk_profiles = {
    101 : {"name": " Ram yadav", "Risk":"High", "Score":1.5},
    102 : {"name": " Aditya yadav", "Risk":"High", "Score":5.2},
    103 : {"name": " Satyam yadav", "Risk":"High", "Score":0.5}
}

@app.get("/customer/{customer_id}")
def profile_check(customer_id:int):
    if customer_id not in customer_risk_profiles :
        return {"error": f"customer {customer_id} not found"}
    
    profile = customer_risk_profiles[customer_id]

    return {
        "customer_id": customer_id,
        "customer_name": profile["name"],
        "Risk": profile["Risk"],
        "Scrore":profile['Score']
    }


@app.get("/model/{model_name}/customer/{customer_id}")
def model_name_check(model_name: str, customer_id: int):
    return {"mode_name":model_name,
            "customer_id": customer_id,
            "predication": "high risk",
            }


@app.get("/customers/")
def get_customer(city:str, risk: int):
    return { "City": city,
            "Risk": risk}