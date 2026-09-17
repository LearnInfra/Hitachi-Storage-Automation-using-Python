import requests
from requests.auth import HTTPBasicAuth
from urllib3.exceptions import InsecureRequestWarning

# Suppress SSL warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Storage credentials
VSP_IP = "10.10.10.100"
USERNAME = "storageadmin"
PASSWORD = "password"

url = f"https://{VSP_IP}/ConfigurationManager/v1/objects/pools"

response = requests.get(
    url,
    auth=HTTPBasicAuth(USERNAME, PASSWORD),
    verify=False
)

response.raise_for_status()

pools = response.json()["data"]

print("\nPool Utilization Report")
print("-" * 80)

for pool in pools:
    pool_id = pool["poolId"]
    pool_name = pool.get("poolName", "N/A")

    total = float(pool["totalCapacity"])
    used = float(pool["usedCapacity"])

    utilization = (used / total) * 100 if total > 0 else 0

    print(
        f"Pool ID: {pool_id:3} | "
        f"Name: {pool_name:20} | "
        f"Used: {utilization:6.2f}%"
    )
