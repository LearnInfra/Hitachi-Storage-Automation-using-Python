import requests
from requests.auth import HTTPBasicAuth
from urllib3.exceptions import InsecureRequestWarning

# Suppress SSL warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

VSP_IP = "10.10.10.100"
USERNAME = "storageadmin"
PASSWORD = "password"

url = f"https://{VSP_IP}/ConfigurationManager/v1/objects/remote-mirror-copypairs"

response = requests.get(
    url,
    auth=HTTPBasicAuth(USERNAME, PASSWORD),
    verify=False
)

response.raise_for_status()

pairs = response.json()["data"]

print("\nReplication Pair Status")
print("-" * 120)

for pair in pairs:
    print(
        f"PairID: {pair['copyGroupName']:<15} "
        f"P-VOL: {pair['pvolLdevId']:<6} "
        f"S-VOL: {pair['svolLdevId']:<6} "
        f"Status: {pair['status']:<10} "
        f"Type: {pair['mirrorUnitId']}"
    )
