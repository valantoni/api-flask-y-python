import requests

# URL of the API endpoint you want to send the request to
url = "http://127.0.0.1:5000/submit"

# Data to be sent in the request body (two variables)
data = {
    "name": "toni",
    "email": "toni@hotmail.com"
}

# Send the POST request with the data in the body
response = requests.post(url, json=data)

# Check the response status code and content
if response.status_code == 200:
    print("Request was successful!")
    print("Response JSON:", response.json())
else:
    print("Request failed with status code:", response.status_code)
    print("Error message:", response.text)
