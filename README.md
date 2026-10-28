# Student Performance Prediction API

A machine learning project that predicts student exam scores using a trained Random Forest regression model. The model is served through FastAPI, containerized using Docker, and tested automatically using GitHub Actions CI.

## Features

- Student exam score prediction using machine learning
- Data preprocessing for numerical and categorical features
- REST API built with FastAPI
- Interactive API documentation using Swagger UI
- Automated API tests using pytest
- Docker containerization
- Continuous Integration using GitHub Actions

## Technology Stack

- **Language:** Python
- **Machine Learning:** scikit-learn, pandas
- **Model Persistence:** joblib
- **API Framework:** FastAPI
- **ASGI Server:** Uvicorn
- **Testing:** pytest, FastAPI TestClient
- **Containerization:** Docker
- **CI/CD:** GitHub Actions

## Project Structure

```text
student-performance-api/
├── .github/
│   └── workflows/
│       └── ci.yml
├── tests/
│   └── test_main.py
├── .dockerignore
├── .gitignore
├── Dockerfile
├── main.py
├── model.joblib
├── requirements.txt
└── README.md
```

## Machine Learning Model

The model was trained in Google Colab using the Student Performance Factors dataset obtained from Kaggle.

The workflow includes:

1. Loading and inspecting the dataset.
2. Separating input features from the target variable, `Exam_Score`.
3. Splitting the dataset into training and testing sets.
4. Handling missing numerical and categorical values.
5. Encoding categorical features using OneHotEncoder.
6. Training a Random Forest Regressor.
7. Evaluating the model using MAE, RMSE, and R².
8. Saving the trained preprocessing and prediction pipeline as `model.joblib`.

The saved pipeline is loaded by the FastAPI application to make predictions on new student data.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Returns an API status message |
| GET | `/health` | Checks API health |
| POST | `/predict` | Predicts a student's exam score |
| GET | `/docs` | Interactive Swagger API documentation |

### Example Prediction Request

```json
{
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
```

### Example Prediction Response

```json
{
  "predicted_exam_score": 67.52
}
```

The response above is an illustrative example of the API output format. Actual predictions depend on the input and trained model.

## Local Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd student-performance-api
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with the URL of this repository.

### 2. Create and activate a virtual environment

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Start the API

```bash
python -m uvicorn main:app --reload
```

Open the following URLs:

- API: http://127.0.0.1:8000/
- Health check: http://127.0.0.1:8000/health
- Swagger documentation: http://127.0.0.1:8000/docs

## Testing

Run the automated tests with:

```bash
python -m pytest tests -v
```

The test suite checks:

- The home endpoint
- The health endpoint
- Successful predictions
- Rejection of invalid input

## Docker

Build the Docker image:

```bash
docker build -t student-performance-api .
```

Run the container:

```bash
docker run --rm -p 8000:8000 student-performance-api
```

Access the API at http://localhost:8000/docs.

## GitHub Actions CI

The workflow is defined in `.github/workflows/ci.yml`.

It runs automatically on pushes to `main` and pull requests targeting `main`. The workflow:

1. Checks out the repository.
2. Sets up Python.
3. Installs the project dependencies.
4. Runs the pytest test suite.
5. Builds the Docker image.

The pipeline is successful when all tests pass and the Docker image builds successfully.

## Model Evaluation

The model was evaluated using Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and R² score on the held-out test set.

Add the actual evaluation values from the Google Colab notebook here before submitting the project.

## Limitations

- Predictions are estimates and are not guaranteed to match actual exam scores.
- Model performance depends on the quality and representativeness of the training data.
- The saved model must be loaded using a compatible scikit-learn version.
- This project is intended for educational and demonstration purposes.

## Future Improvements

- Add model versioning and experiment tracking.
- Improve API input validation and error handling.
- Add model monitoring and prediction logging.
- Deploy the API to a cloud hosting platform.
