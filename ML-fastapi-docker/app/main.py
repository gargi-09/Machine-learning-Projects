from fastapi import FastAPI
from pydantic import BaseModel
from app.model.model import predict_pipe

app = FastAPI()

class Features(BaseModel):
    Married: int
    Dependents: int
    Education: int
    Self_Employed: int
    ApplicantIncome: int
    CoapplicantIncome: int
    LoanAmount: int
    Loan_Amount_Term: int
    Credit_History: int
    Gender_Male: int
    Property_Semiurban: int
    Property_Urban: int

class PredictionOut(BaseModel):
    application_status: int

@app.get("/")
def home():
    return {"health_check":"ok"}

@app.post("/predict",response_model=PredictionOut)
def predict(payload: Features):
    status = predict_pipe([payload.Married,payload.Dependents,payload.Education,payload.Self_Employed,
                           payload.ApplicantIncome,payload.CoapplicantIncome,payload.LoanAmount,
                           payload.Loan_Amount_Term,payload.Credit_History,payload.Gender_Male,
                           payload.Property_Semiurban,payload.Property_Urban])
    return {"Status":status}