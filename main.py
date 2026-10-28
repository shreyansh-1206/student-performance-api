
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI(title="Student Performance Prediction API")

model = joblib.load("model.joblib")


class StudentData(BaseModel):
    Hours_Studied: float
    Attendance: float
    Parental_Involvement: str | None = None
    Access_to_Resources: str | None = None
    Extracurricular_Activities: str | None = None
    Sleep_Hours: float
    Previous_Scores: float
    Motivation_Level: str | None = None
    Internet_Access: str | None = None
    Tutoring_Sessions: float
    Family_Income: str | None = None
    Teacher_Quality: str | None = None
    School_Type: str | None = None
    Peer_Influence: str | None = None
    Physical_Activity: float
    Learning_Disabilities: str | None = None
    Parental_Education_Level: str | None = None
    Distance_from_Home: str | None = None
    Gender: str | None = None


@app.get("/")
def home():
    return {"message": "Student Performance Prediction API is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/predict")
def predict(data: StudentData):
    input_data = pd.DataFrame([data.model_dump()])
    prediction = model.predict(input_data)[0]

    return {"predicted_exam_score": round(float(prediction), 2)}
