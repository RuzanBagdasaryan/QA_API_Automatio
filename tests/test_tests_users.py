from schemas.schemas.user_schema import validate_user_structure
import pytest
import json
import os

def test_get_users(client):
    response = client.get("/users")

    assert response.status_code == 200

    users = response.json()

    for user in users:
        validate_user_structure(user)


def test_user_not_found(client):
    response = client.get("/users/9999")
    assert response.status_code == 404

@pytest.mark.parametrize("user_id, expected_name", [
    (1, "Leanne Graham"),
    (2, "Ervin Howell")
])
def test_user_names(client, user_id, expected_name):
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == expected_name



