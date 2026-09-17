import requests
import json
from requests.auth import HTTPBasicAuth

# VSP Management IP
VSP_IP = "10.10.10.100"
USERNAME = "storageadmin"
PASSWORD = "password"

# Disable certificate warning for self-signed certs
requests.packages.urllib3.disable_warnings()

# REST API endpoint
url = f"https://{VSP_IP}/ConfigurationManager/v1/objects/ldevs"

# LDEV parameters
payload = {
    "poolId": 0,
    "blockCapacity": 21474836480,
    "dataReductionMode": "disabled",
    "isParallelExecutionEnabled": True
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(
    url,
    auth=HTTPBasicAuth(USERNAME, PASSWORD),
    headers=headers,
    json=payload,
    verify=False
)

print(f"HTTP Status: {response.status_code}")
print(json.dumps(response.json(), indent=4))
