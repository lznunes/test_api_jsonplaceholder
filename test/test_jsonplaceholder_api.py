import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.mark.parametrize("resource", ["posts", "comments", "users"])
def test_get_resources(resource):
    response = requests.get(f"{BASE_URL}/{resource}")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_get_single_resource():
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert "title" in data
    assert "body" in data
    assert "userId" in data


def test_create_resource():
    payload = {"title": "foo", "body": "bar", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]


def test_update_resource():
    payload = {"title": "foo", "body": "bar", "userId": 1}
    response = requests.put(f"{BASE_URL}/posts/1", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]


def test_patch_resource():
    payload = {"title": "foo"}
    response = requests.patch(f"{BASE_URL}/posts/1", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == payload["title"]


def test_delete_resource():
    response = requests.delete(f"{BASE_URL}/posts/1")
    assert response.status_code == 200
