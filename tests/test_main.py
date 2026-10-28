
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_predict():
    payload = {
        "Hours_Studied": 5,
        "Attendance": 90,
        "Parental_Involvement": "High",
        "Access_to_Resources": "High",
        "Extracurricular_Activities": "Yes",
        "Sleep_Hours": 7,
        "Previous_Scores": 75,
        "Motivation_Level": "High",
        "Internet_Access": "Yes",
        "Tutoring_Sessions": 2,
        "Family_Income": "Medium",
        "Teacher_Quality": "High",
        "School_Type": "Public",
        "Peer_Influence": "Positive",
        "Physical_Activity": 3,
        "Learning_Disabilities": "No",
        "Parental_Education_Level": "College",
        "Distance_from_Home": "Near",
        "Gender": "Female"
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 200
    assert isinstance(response.json()["predicted_exam_score"], (int, float))


def test_predict_invalid_input():
    response = client.post("/predict", json={"Hours_Studied": "invalid"})
    assert response.status_code == 422
