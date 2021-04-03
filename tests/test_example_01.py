import requests


def test_get_status_code_200():
    response = requests.get("http://api.zippopotam.us/us/90210")
    assert response.status_code == 200
    print(response.status_code)

def test_get_content_type():
    response = requests.get("http://api.zippopotam.us/us/90210")
    assert response.headers["Content-Type"] == "application/json"
    print(response.headers["Content-Type"])


def test_get_body_encoding_not_set_equal_to_none():
    response = requests.get("http://api.zippopotam.us/us/90210")
    response_body = response.json()
    assert response.encoding is None
    print(response.encoding)


def test_get_body_response_with_value():
    response = requests.get("http://api.zippopotam.us/us/90210")
    response_body = response.json()
    assert response_body["country"] == "United States"
    print(response_body["country"])


def test_get_place_name_from_body():
    response = requests.get("http://api.zippopotam.us/us/90210")
    response_body = response.json()
    assert response_body["places"][0]["place name"] == "Beverly Hills"
    print(response_body["places"][0]["place name"])


def test_get_places_length():
    response = requests.get("http://api.zippopotam.us/us/90210")
    response_body = response.json()
    assert len(response_body["places"]) == 1
    print(len(response_body["places"]))