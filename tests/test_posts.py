def test_create_post(client):
    payload = {
        "title": "Automation Test",
        "body": "QA portfolio project",
        "userId": 1
    }

    response = client.post("/posts", payload)

    assert response.status_code == 201

    data = response.json()
    assert data["title"] == "Automation Test"
    assert data["userId"] == 1
