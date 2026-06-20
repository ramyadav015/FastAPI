from fastapi import FastAPI
from pydantic import BaseModel, Field
from enum import Enum

app = FastAPI()

class GenderEnum(str , Enum):
    male = "male"
    female = "female"

class SmokerEnum(str, Enum):
    Yes = "Yes"
    No= "No"

class RegionEnum(str, Enum):
    northeast = "northeast"
    northwest = "northwest"
    southeast = "southeast"
    southwest = "southwest"


class health_insurance_validate_data(BaseModel):
    age : int =Field(ge=18, le=100)
    gender: GenderEnum
    BMI : float = Field(ge=10, le=60)
    no_of_children : int = Field(ge=0, le=5)
    smoker : SmokerEnum
    region : RegionEnum

@app.get("/health")
def display():

    return (" Yes, I am working. How may I help you? ")

@app.post("/predict")
def prediction_health(health:health_insurance_validate_data):

    if health.smoker == SmokerEnum.Yes and health.age >40:
        price = 1200
    elif health.smoker == SmokerEnum.No and health.age <=40:
        price = 800
    elif health.age > 40:
        price = 650
    elif health.BMI >30:
        price = 550
    else:
        price = 330
    
    return {"age":health.age,
            "BMI": health.BMI,
            "Gender":health.gender,
             "Smoker":health.smoker,
              "region":health.region,
              "Health insurance Charges - ":price 
             }