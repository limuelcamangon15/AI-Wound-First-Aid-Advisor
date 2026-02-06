from app.schemas import WoundAssessmentRequest

def apply_safety_rules(data: WoundAssessmentRequest, ml_risk: str) -> dict:
    reasons = []
    final_risk = ml_risk
    doctor_visit = False

    if data.bleeding == "continuous":
        final_risk = "HIGH"
        doctor_visit = True
        reasons.append("Continuous bleeding detected")
    
    if data.pus:
        final_risk = "HIGH"
        doctor_visit = True
        reasons.append("Possible infection (pus present)")

    if data.depth == "deep":
        final_risk = "HIGH"
        doctor_visit = True
        reasons.append("Deep wound")

    if data.pain_level >= 8:
        final_risk = "HIGH"
        doctor_visit = True
        reasons.append("Severe pain")

    if final_risk != "HIGH":
        if data.swelling and data.redness:
            final_risk = "MODERATE"
            reasons.append("Inflammation signs detected")

    return{
        "final_risk": final_risk,
        "doctor_visit": doctor_visit,
        "reasons": reasons
    }