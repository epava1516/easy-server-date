import json
import requests

# Load the data from the JSON file
with open("all_hosts.json", 'r') as f:
    data = json.load(f)

# Specify the Centreon API URL
api_url = "http://10.250.211.45/centreon/api/index.php"

# Specify your Centreon API credentials
api_credentials = {
    "username": "admin",
    "password": "Cent0s123!321"
}

# Log in to the Centreon API
response = requests.post(f"{api_url}?action=authenticate", data=api_credentials)
api_token = response.json()

# Set up the headers for the API requests
headers = {
    "Content-Type": "application/json",
    "centreon-auth-token": api_token["authToken"]
}

# Iterate over the hostgroups in the data
for host in data['result']:
    # Prepare the host data
    host_data = {
        "action": "add",
        "object": "host",
        "values": f"{host['name']};{host['alias']};{host['address_ip']};OS-Windows-NRPE-custom;central;1_Acabados;" 
        # Modify this line as needed to match your Centreon configuration
    }
    
    # Send a POST request to the Centreon API to add the host
    response = requests.post(f"{api_url}?action=action&object=centreon_clapi", headers=headers, data=json.dumps(host_data))

    # Check if the request was successful
    if response.status_code == 200:
        print(f"Successfully added host {host['name']}")
    else:
        print(f"Failed to add host {host['name']}: {response.status_code} {response.reason} {response.text}")

