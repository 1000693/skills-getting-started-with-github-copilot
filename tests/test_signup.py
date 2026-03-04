def test_signup_happy_path_adds_participant(client):
    email = "test_student@mergington.edu"
    activity = "Chess Club"

    # Ensure not already present
    res = client.get("/activities")
    assert res.status_code == 200
    before = res.json()
    assert email not in before[activity]["participants"]

    # Signup
    post = client.post(f"/activities/{activity}/signup?email={email}")
    assert post.status_code == 200
    assert "Signed up" in post.json().get("message", "")

    # Verify participant added
    res2 = client.get("/activities")
    after = res2.json()
    assert email in after[activity]["participants"]


def test_signup_duplicate_returns_400(client):
    email = "duplicate@mergington.edu"
    activity = "Programming Class"

    # First signup should succeed
    r1 = client.post(f"/activities/{activity}/signup?email={email}")
    assert r1.status_code == 200

    # Second signup should fail with 400
    r2 = client.post(f"/activities/{activity}/signup?email={email}")
    assert r2.status_code == 400
    assert r2.json().get("detail") == "Student is already signed up"
