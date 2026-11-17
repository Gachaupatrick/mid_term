import requests, json

# 1. Load the sample SKU from the data folder
with open("data/sku_3500.json", "r") as f:
    sku_3500 = json.load(f)

# The URL of your running Flask app endpoint
url = "http://127.0.0.1:9696/predict"

# Send POST request with JSON data
response = requests.post(url, json=sku_3500)

# Print the resulting JSON response from your Flask app
print(response.json())