
import requests
import json



headers = {
    "Authorization" : "Bearer ht4b6M6jOYJO5hIEIxQB" 
}

sda = requests.get("https://the-one-api.dev/v2/movie", headers=headers)
sda = sda.json()
print(sda)