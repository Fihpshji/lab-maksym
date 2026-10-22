import pytest

import app as app_module


@pytest.fixture
def client():
    app_module.tasks.clear()
    return app_module.app.test_client()


def test_add_task(client):
    r = client.post("/api/tasks", json={"title": "Lab 1", "deadline": "2026-11-01"})
    assert r.status_code == 201
    assert r.get_json()["id"] == 1


def test_add_task_without_title(client):
    assert client.post("/api/tasks", json={}).status_code == 400


def test_list_tasks(client):
    client.post("/api/tasks", json={"title": "Lab 1"})
    r = client.get("/api/tasks")
    assert r.status_code == 200
    assert len(r.get_json()) == 1
