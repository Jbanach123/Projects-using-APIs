import requests
from datetime import datetime
import os

APP_ID = os.environ["APP_ID"]   
API_KEY = os.environ["API_KEY"]  
exercise_in = input("Tell me which exercise you did: ")
excercise_endpoint = f"https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = os.environ["SHEET_ENDPOINT"] 

# Type your parameters
excercise_params = {
    "query": exercise_in,
    "gender": "male",
    "weight_kg": 80,
    "height_cm": 180,
    "age": 20
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

response = requests.post(url=excercise_endpoint, json=excercise_params, headers=headers)
result = response.json()
#print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
time_now = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_header = {
        "Authorization": f"Bearer {os.environ["BEARER_TOKEN"]}"
    }

    sheet_response = requests.post(url=SHEET_ENDPOINT, json=sheet_inputs, headers=sheet_header)
    print(sheet_response.text)
