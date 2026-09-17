import requests
from requests.auth import HTTPBasicAuth
import matplotlib.pyplot as plt

# VSP Details
VSP_IP = "10.10.10.100"
USERNAME = "storageadmin"
PASSWORD = "password"

# Disable SSL verification warning
requests.packages.urllib3.disable_warnings()

url = f"https://{VSP_IP}/ConfigurationManager/v1/objects/pools"

response = requests.get(
    url,
    auth=HTTPBasicAuth(USERNAME, PASSWORD),
    verify=False
)

response.raise_for_status()

pool_names = []
utilization_values = []

for pool in response.json()["data"]:
    name = pool.get("poolName", f"Pool-{pool['poolId']}")
    total = float(pool["totalCapacity"])
    used = float(pool["usedCapacity"])

    utilization = (used / total) * 100 if total > 0 else 0

    pool_names.append(name)
    utilization_values.append(utilization)

# Create chart
plt.figure(figsize=(10, 6))
bars = plt.bar(pool_names, utilization_values)

# Color coding
for bar, value in zip(bars, utilization_values):
    if value >= 90:
        bar.set_color("red")
    elif value >= 80:
        bar.set_color("orange")
    else:
        bar.set_color("green")

plt.axhline(y=80, color='orange', linestyle='--', label='Warning (80%)')
plt.axhline(y=90, color='red', linestyle='--', label='Critical (90%)')

plt.title("Hitachi VSP Pool Utilization")
plt.xlabel("Pool Name")
plt.ylabel("Utilization (%)")
plt.ylim(0, 100)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show percentage labels
for i, val in enumerate(utilization_values):
    plt.text(i, val + 1, f"{val:.1f}%", ha='center')

plt.tight_layout()
plt.show()
