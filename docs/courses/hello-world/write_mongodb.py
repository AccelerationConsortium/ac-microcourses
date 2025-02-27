import json  # noqa: F401

import requests
from my_secrets import COURSE_ID, LAMBDA_FUNCTION_URL, PASSWORD, SSID
from netman import connectWiFi

connectWiFi(SSID, PASSWORD, country="US")

document = {"course_id": COURSE_ID}

response = requests.post(LAMBDA_FUNCTION_URL, json=document)

if response.status_code == 200:
    response_data = response.json()
    print(response_data["message"])
else:
    print(f"Request failed with status code {response.status_code}")
