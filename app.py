from fastapi import FastAPI
from pydantic import BaseModel
from predictor import predict_anemia

class JumlahInput(BaseModel):
    a: int
    b: int

class Lingkaran(BaseModel):
    radius: int

class AnemiaInput(BaseModel):
    rbc : float
    hgb : float
    hct : float
    mcv : float
    mch : float
    mchc : float
    rdw : float

app  =FastAPI()


@app.post("/predict-anemia")
def predict_anemia_endpoint(data: AnemiaInput):
    result = predict_anemia(
        rbc=data.rbc,
        hgb=data.hgb,
        hct=data.hct,
        mcv=data.mcv,
        mch=data.mch,
        mchc=data.mchc,
        rdw=data.rdw,

    )

    return{
        "prediction": result
    }
    
