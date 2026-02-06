from fastapi import FastAPI
from app.schemas import (WoundAssessmentRequest, WoundAssessmentResponse)

app = FastAPI(
    title="AI Wound First-Aid Advisor",
    description="An AI-assisted wound first-aid advisor and suggestion tool",
    version="0.1.0"
)

@app.get("/health")
def root():
    return {
            "message": "Hello Machine Learning!",
            "status": "ok"
            }

@app.post("/assess", response_model=WoundAssessmentResponse)
def assess_wound(data: WoundAssessmentRequest):

    #test data
    risk_level = "HIGH"
    doctor_visit = True
    first_aid = [
        "Clean the wound with clean running water",
        "Cover with a sterile dressing"
    ]

    
    print({
        "risk_level": risk_level,
        "doctor_visit": doctor_visit,
        "first_aid": first_aid,
        "note": "This tool provides first-aid suggestions only and is not a medical diagnosis."
    })
    
    return {
        "risk_level": risk_level,
        "doctor_visit": doctor_visit,
        "first_aid": first_aid,
        "note": "This tool provides first-aid suggestions only and is not a medical diagnosis."
    }
    
