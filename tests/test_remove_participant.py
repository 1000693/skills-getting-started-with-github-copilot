def test_remove_participant_happy_path(client):
    # Use an existing participant from initialized data
    activity = "Chess Club"
    email = "michael@mergington.edu"

    # Ensure present
    res = client.get("/activities")
    assert res.status_code == 200
    assert email in res.json()[activity]["participants"]

    # Remove participant
    r = client.delete(f"/activities/{activity}/participants?email={email}")
    assert r.status_code == 200
    assert "Removed" in r.json().get("message", "")

    # Verify removed
    res2 = client.get("/activities")
    assert email not in res2.json()[activity]["participants"]


def test_remove_nonexistent_participant_returns_404(client):
    activity = "Tennis Club"
    email = "notfound@mergington.edu"

    r = client.delete(f"/activities/{activity}/participants?email={email}")
    assert r.status_code == 404
    assert r.json().get("detail") == "Participant not found"


def test_participants_list_updates_after_remove(client):
    activity = "Gym Class"
    email = "john@mergington.edu"

    # Confirm present
    res = client.get("/activities")
    assert email in res.json()[activity]["participants"]

    # Remove and then get activities to confirm
    client.delete(f"/activities/{activity}/participants?email={email}")
    res2 = client.get("/activities")
    assert email not in res2.json()[activity]["participants"]
