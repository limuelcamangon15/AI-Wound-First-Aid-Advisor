from typing import List
from pydantic import BaseModel, Field
from enum import Enum

class BleedingLevel(str, Enum):
    none = "none"
    mild = "mild"
    continuous = "continuous"

class WoundDepth(str, Enum):
    surface = "surface"
    moderate = "moderate"
    deep = "deep"

class WoundAssessmentRequest(BaseModel):
    bleeding: BleedingLevel
    depth: WoundDepth
    pain_level: int = Field(..., ge=1, le=10)
    swelling: bool
    redness: bool
    pus:bool

class WoundAssessmentResponse(BaseModel):
    risk_level: str
    doctor_visit: bool
    first_aid: List[str]
    note: str