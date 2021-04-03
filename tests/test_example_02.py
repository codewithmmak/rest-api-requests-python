import pytest, requests, csv


test_data_zip = [
    ("us", "90210", "Beverly Hills"),
    ("it", "50123", "Firenze"),
    ("ca", "Y1A", "Whitehorse"),
]


@pytest.mark.parametrize("country_code, zip_code, expected_place", test_data_zip)
def test_get_location_data_check_place_name(country_code, zip_code, expected_place):
    response = requests.get(f"http://api.zippopotam.us/{country_code}/{zip_code}")
    response_body = response.json()
    assert response_body["places"][0]["place name"] == expected_place
    print(response_body["places"][0]["place name"])


def read_data_from_csv():
    test_data_users_from_csv = []
    with open("test-data/test-data-zip.csv", newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        for row in data:
            test_data_users_from_csv.append(row)
    return test_data_users_from_csv


@pytest.mark.parametrize("country_code, zip_code, expected_place", read_data_from_csv())
def test_get_location_data_check_place_name_from_csv(country_code, zip_code, expected_place):
    response = requests.get(f"http://api.zippopotam.us/{country_code}/{zip_code}")
    response_body = response.json()
    assert response_body["places"][0]["place name"] == expected_place
    print(response_body["places"][0]["place name"])