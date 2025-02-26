import json  # noqa: F401

import requests
from my_secrets import ATLAS_URI, COURSE_ID, PASSWORD, SSID
from netman import connectWiFi

connectWiFi(SSID, PASSWORD, country="US")

document = {"course_id": COURSE_ID}

response = requests.post(ATLAS_URI, json=document)

if response.status_code == 200:
    response_data = response.json()
    print(response_data["message"])
else:
    print(f"Request failed with status code {response.status_code}")
