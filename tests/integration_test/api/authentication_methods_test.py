from src.utils.settings import FAKE_TOKEN
from tests.conftest import client

email = 'test@test3.com'
password = '12345'
user_endpoint = '/users/'


def test_basic_auth():
    client.post(user_endpoint, json={'email': email, 'password': password})
    basic_auth_response = client.get('/basic-auth', auth=(email, password))
    json_response = basic_auth_response.json()

    assert basic_auth_response.status_code == 200
    assert json_response['message'] == 'Authenticated'
    assert json_response['username'] == email


def test_bearer_auth():
    client.post(user_endpoint, json={'email': email+'bearer', 'password': password})
    bearer_auth_response = client.get('/bearer-auth', headers={'Authorization': f'Bearer {FAKE_TOKEN}'})
    json_response = bearer_auth_response.json()

    assert bearer_auth_response.status_code == 200
    assert json_response['message'] == 'Authenticated'
    assert json_response['token'] == FAKE_TOKEN


def test_jwt_auth():
    client.post(user_endpoint, json={'email': email+'jwt', 'password': password})
    jwt_auth_response = client.post('/jwt-auth', data={'username': email+'jwt', 'password': password})
    json_jwt_auth_response = jwt_auth_response.json()
    bearer_jwt_auth_response = client.get('/jwt-auth-bearer', headers={'Authorization': f'Bearer {json_jwt_auth_response["access_token"]}'})
    json_bearer_jwt_auth_response = bearer_jwt_auth_response.json()

    assert json_jwt_auth_response['token_type'] == 'bearer'
    assert json_bearer_jwt_auth_response['message'] == 'Authenticated'
    assert json_bearer_jwt_auth_response['user'] == email+'jwt'
