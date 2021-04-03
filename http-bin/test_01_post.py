# import requests
# import json
#
#
# def test_post_status_code():
#
#     # Endpoint or URI
#     url = "http://httpbin.org/post"
#
#     # Payload or body of request
#     # payload = "{\r\n    \"key1\": 1,\r\n    \"key2\": \"value2\"\r\n}"
#     payload = ""
#
#     # Headers
#     headers = {'Content-Type': 'text/plain'}
#
#     # convert dict to json string by json.dumps() for body data.
#     response = requests.post(url, headers=headers, data=json.dumps(payload))
#
#     # Validate response headers and body contents, e.g. status code.
#     assert response.status_code == 200
#
#     response_body = response.json()
#     assert response_body['url'] == url
#
#     # print response full body as text
#     print(response.text)
