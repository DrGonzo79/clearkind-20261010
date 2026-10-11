from fastapi.testclient import TestClient
from main import TriageRequest, app, load_fixture, triage_item
client = TestClient(app)

def test_sentimental_item_is_held():
    r=client.post("/triage",json={"item_id":"EST-104","sentiment":"keep","days_remaining":10})
    assert r.status_code==200 and r.json()["route"]=="family_hold" and r.json()["fictional"] is True

def test_wide_value_range_gets_expert_review():
    r=client.post("/triage",json={"item_id":"EST-103","sentiment":"release","days_remaining":4})
    assert r.status_code==200 and r.json()["route"]=="expert_review"

def test_invalid_timeline_is_rejected():
    assert client.post("/triage",json={"item_id":"EST-101","sentiment":"unsure","days_remaining":0}).status_code==422

def test_unknown_item_is_visible():
    r=client.post("/triage",json={"item_id":"NOPE","sentiment":"unsure","days_remaining":10})
    assert r.status_code==404 and r.json()["detail"]=="Demo item not found"

def test_fixture_failure_is_visible(monkeypatch):
    import main
    monkeypatch.setattr(main,"load_fixture",lambda: (_ for _ in ()).throw(FileNotFoundError()))
    r=client.post("/triage",json={"item_id":"EST-101","sentiment":"unsure","days_remaining":10})
    assert r.status_code==503 and r.json()["detail"]=="Estate fixture is unavailable"

def test_domain_operation_directly():
    item=load_fixture()["items"][0]
    result=triage_item(item,TriageRequest(item_id=item["id"],sentiment="release",days_remaining=12))
    assert result["route"]=="expert_review"
