from tests.conftest import client

email = 'test@test2.com'

def test_create_user():
    response = client.post('/users/', json={'email': email, 'password': '12345'})
    assert response.status_code == 200
    assert response.json()['message'] == 'User created successfully.'


def test_get_user():
    response = client.post('/users/', json={'email': email+'m', 'password': '12345'})
    json_response = response.json()
    get_response = client.get(f'/users/{json_response.get("id")}')
    assert get_response.status_code == 200
    assert get_response.json()['email'] == email+'m'
