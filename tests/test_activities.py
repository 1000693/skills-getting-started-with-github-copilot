def test_get_activities_returns_mapping(client):
    res = client.get("/activities")
    assert res.status_code == 200
    data = res.json()
    assert isinstance(data, dict)
    # Expect some known activities to be present
    assert "Chess Club" in data
    assert "Programming Class" in data
