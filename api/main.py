from pathlib import Path
import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

FIXTURE_PATH = Path(__file__).resolve().parents[1] / "data" / "demo_items.json"

class TriageRequest(BaseModel):
    item_id: str = Field(min_length=1, max_length=30)
    sentiment: str = Field(pattern="^(keep|unsure|release)$")
    days_remaining: int = Field(ge=1, le=60)

def load_fixture() -> dict:
    if not FIXTURE_PATH.exists():
        raise FileNotFoundError("demo estate fixture is missing")
    return json.loads(FIXTURE_PATH.read_text())

def triage_item(item: dict, request: TriageRequest) -> dict:
    spread = item["estimatedHigh"] - item["estimatedLow"]
    if request.sentiment == "keep":
        route, confidence = "family_hold", "high"
        reasons = ["A family member marked this meaningful", "Preserve first; value can be checked later"]
        next_steps = ["Move to the family hold zone", "Photograph the story or memory", "Assign a family decision owner"]
    elif item["marketClues"] >= 2 and (item["estimatedHigh"] >= 250 or spread >= 400):
        route, confidence = "expert_review", "medium"
        reasons = ["Wide value range makes disposal risky", f"{item['marketClues']} market clues need verification"]
        next_steps = ["Photograph marks, labels, and damage", "Request one specialist opinion", "Do not donate or haul before review"]
    elif item["estimatedHigh"] >= 100 and request.days_remaining >= 7:
        route, confidence = "sell_batch", "medium"
        reasons = ["Plausible resale value clears the demo threshold", f"{request.days_remaining} days allows a short listing window"]
        next_steps = ["Group with similar items", "Set a 7-day decision deadline", "Donate if the batch does not move"]
    else:
        route = "short_hold" if request.sentiment == "unsure" else "donate_recycle"
        confidence = "medium"
        reasons = ["Uncertainty deserves a reversible pause" if request.sentiment == "unsure" else "Low resale signal favors fast release", "Route is reversible until pickup"]
        next_steps = ["Capture one record photo", "Confirm no family claimant", "Choose a local donation or recycling path"]
    return {"fictional": True, "item": item, "route": route, "confidence": confidence, "reasons": reasons, "next_steps": next_steps}

app = FastAPI(title="ClearKind API", version="0.1.0")

@app.get("/health")
def health(): return {"status": "ok", "fixture": "fictional"}

@app.post("/triage")
def triage(request: TriageRequest):
    try: fixture = load_fixture()
    except (FileNotFoundError, json.JSONDecodeError) as exc:
        raise HTTPException(status_code=503, detail="Estate fixture is unavailable") from exc
    item = next((x for x in fixture["items"] if x["id"] == request.item_id), None)
    if item is None: raise HTTPException(status_code=404, detail="Demo item not found")
    return triage_item(item, request)
