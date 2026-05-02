def test_health_check(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json["status"] == "ok"
    assert resp.json["service"] == "task-manager"
