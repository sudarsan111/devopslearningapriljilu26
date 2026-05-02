def test_list_empty(client):
    resp = client.get("/tasks")
    assert resp.status_code == 200
    assert resp.json == []

def test_create_task(client):
    resp = client.post("/tasks", json={"title": "Learn CI/CD", "description": "GitHub Actions"})
    assert resp.status_code == 201
    assert resp.json["title"] == "Learn CI/CD"
    assert resp.json["done"] is False
    assert "id" in resp.json

def test_create_task_missing_title(client):
    resp = client.post("/tasks", json={})
    assert resp.status_code == 400
    assert "error" in resp.json

def test_create_task_empty_title(client):
    resp = client.post("/tasks", json={"title": "   "})
    assert resp.status_code == 400

def test_get_task(client):
    created = client.post("/tasks", json={"title": "Get me"}).json
    resp = client.get(f"/tasks/{created['id']}")
    assert resp.status_code == 200
    assert resp.json["id"] == created["id"]

def test_get_task_not_found(client):
    resp = client.get("/tasks/does-not-exist")
    assert resp.status_code == 404

def test_update_task(client):
    created = client.post("/tasks", json={"title": "Old title"}).json
    resp = client.put(f"/tasks/{created['id']}", json={"title": "New title", "done": True})
    assert resp.status_code == 200
    assert resp.json["title"] == "New title"
    assert resp.json["done"] is True

def test_update_task_not_found(client):
    resp = client.put("/tasks/does-not-exist", json={"title": "x"})
    assert resp.status_code == 404

def test_delete_task(client):
    created = client.post("/tasks", json={"title": "Delete me"}).json
    resp = client.delete(f"/tasks/{created['id']}")
    assert resp.status_code == 204

def test_delete_task_not_found(client):
    resp = client.delete("/tasks/does-not-exist")
    assert resp.status_code == 404

def test_list_after_create(client):
    client.post("/tasks", json={"title": "Task 1"})
    client.post("/tasks", json={"title": "Task 2"})
    resp = client.get("/tasks")
    assert len(resp.json) == 2

def test_deleted_task_not_listed(client):
    created = client.post("/tasks", json={"title": "Temp"}).json
    client.delete(f"/tasks/{created['id']}")
    resp = client.get("/tasks")
    assert resp.json == []
