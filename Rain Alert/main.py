import requests
from twilio.rest import Client

OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
# File empty places with your data
api_key = ""

auth_token = ""
account_sid = ""
# Forecast parameters
parameters = {
    # use your coordinates
    "appid": api_key,
    "lat": ,
    "lon": ,
    "cnt": 
}
# Convert data
response = requests.get(OWM_endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for data in weather_data["list"]:
    weather_id = data["weather"][0]["id"]
    if int(weather_id) < 700:
        will_rain = True
if will_rain:
    # Sending an SMS
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Dziś będzie padał deszcz. Zabierz parasol ☔.",
        from_=""
        to=""
    )
    print(message.status)
