import pytest


@pytest.mark.parametrize(
    "url", ["/users/details", "/users?name=Graham", "/users/websites"]
)
def test_should_not_get_users_routes(client, url):
    headers = {"Authorization": "Bearer " + "invalid token"}
    result = client.get(url, headers=headers)
    assert result.status_code == 403
    assert result.json()["detail"] == "Invalid authorization"


def test_should_get_users_details(client, get_token):
    headers = {"Authorization": "Bearer " + get_token}
    result = client.get("/users/details", headers=headers)
    assert result.status_code == 200
    assert len(result.json()["users"]) == 10


def test_should_get_users_by_word(client, get_token):
    headers = {"Authorization": "Bearer " + get_token}
    result = client.get("/users?name=Graham", headers=headers)
    assert result.status_code == 200
    assert result.json()["users"][0]["name"] == "Leanne Graham"


def test_should_get_user_websites(client, get_token):
    headers = {"Authorization": "Bearer " + get_token}
    result = client.get("/users/websites", headers=headers)
    assert result.status_code == 200
    assert len(result.json()["websites"]) == 10
